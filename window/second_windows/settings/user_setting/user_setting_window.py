"""
Переделать логику
"""

import os

from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QRegion, QColor
from PIL import Image

from window.data_class_for_window.dataclass import BaseDataclassWindows
from window.second_windows.settings.user_setting.user_class import Ui_Dialog, QDialog, QPixmap, Qt, QPainter


from functions.settings.settings import load_theme
from data_base.test_orm import update_image, update_user, select_User, User
from functions.walidation.walid_password import check_password_strength


class UserSettingsDialog(QDialog):
    """
    Класс окна настроек интерфейса
    """
    def __init__(self, user_id: int):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.state = BaseDataclassWindows(
            theme= load_theme(self)
        )

        self.user_id = user_id
        self.image = None
        self.__start()
        self.ui.push_button_chose_image.clicked.connect(self.__chose_image)
        self.ui.push_button_save.clicked.connect(self.__save)

    def __start(self):
        user: User = select_User(user_id= self.user_id)
        self.ui.linedit_username.setText(user.username)
        if user.image:
            self.setCircleImage(user.image)

    def __chose_image(self):
        filedialog = QFileDialog()
        # тут доделать параметры
        self.image = filedialog.getOpenFileName(caption='Выбрать файл'
                                                    )
        
        if self.image != ('', ''):
            self.setCircleImage(self.image[0])

    def __save(self):
        self.__save_image()
        self.__save_user()

    def __save_image(self):
        # потои переделать с исключениями
        
        if self.image is not None:
            img = Image.open(self.image[0])
            img = img.convert('RGB')
            path = f'Data\\Data_base\\image\\{os.path.splitext(os.path.basename(self.image[0]))[0]}.jpg'
            img.save(path, 'JPEG', quality=70)

            update_image(
                    user_id= self.user_id,
                    image = path
                )
            return True
        return None

    def __save_user(self):

        user: User = select_User(user_id= self.user_id)
        user_name = None
        password = None
        if self.ui.linedit_username.text() != user.username:
            user_name = self.ui.linedit_username.text()

        empty = self.ui.linedit_password.text() != ''
        old_password = self.ui.linedit_password.text() != user.password

        if empty and old_password and check_password_strength(self.ui.linedit_password.text())[0]:
    
            password= self.ui.linedit_password.text()
            self.ui.label_walidation_password.setText(
                'Пароль сохронён'
            )
        else:
            if not old_password:
                self.ui.label_walidation_password.setText(
                "<p style='color: red'>Укажите новый пароль</p>"
            )
            elif not check_password_strength(self.ui.linedit_password.text())[0] and empty:
                self.ui.label_walidation_password.setText(
                    f"<p style='color: red'>{check_password_strength(self.ui.linedit_password.text())[1]}</p>"
                )
        if user_name or password:
            update_user(
                user_id= self.user_id,
                username= user_name,
                password= password
            )
    def createCircleMask(self, size, x, y):
        mask = QPixmap(size, size)
        mask.fill(Qt.transparent)
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        # Центрируем круг внутри области
        painter.setBrush(QColor("black"))
        # Рисуем круг в центре своей области
        painter.drawEllipse(x, y, size, size)
        painter.end()
        region = QRegion(mask.mask())
        return region

    def setCircleImage(self, image_path):
        orig_pixmap = QPixmap(image_path)
        desired_size = self.ui.label_image.size().height()
        if orig_pixmap.isNull():
            orig_pixmap = QPixmap(r'Data\Data_base\image\8hOlH9yPHi7DbakNO6XafkdRmjw3DANbj2ojvQqw.jpg')

        min_ = min(orig_pixmap.size().width(), orig_pixmap.size().height())
        if min_ == orig_pixmap.size().width():
            c = orig_pixmap.size().height() / orig_pixmap.size().width() * desired_size
            orig_pixmap = orig_pixmap.scaled(desired_size, c , Qt.KeepAspectRatio, Qt.SmoothTransformation)
            sx = 0
            sy = (orig_pixmap.size().height() - orig_pixmap.size().width()) /2
        else:
            c = orig_pixmap.size().width() / orig_pixmap.size().height() * desired_size
            orig_pixmap = orig_pixmap.scaled(c, desired_size , Qt.KeepAspectRatio, Qt.SmoothTransformation)
            sx = (orig_pixmap.size().width() - orig_pixmap.size().height()) /2
            sy = 0


        target_pixmap = QPixmap(desired_size, desired_size)
        target_pixmap.fill(Qt.transparent)

        painter = QPainter(target_pixmap)
        reg  = self.createCircleMask(desired_size, 0, 0)

        painter.setClipRegion(reg)

        painter.drawPixmap(0, 0, orig_pixmap, sx , sy, desired_size, desired_size)
        painter.end()
        self.ui.label_image.setPixmap(target_pixmap)
