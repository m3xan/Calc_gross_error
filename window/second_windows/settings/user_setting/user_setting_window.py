"""
Переделать логику
"""

import os

from PySide6.QtWidgets import QFileDialog
from PIL import Image

from window.data_class_for_window.dataclass import BaseDataclassWindows
from window.second_windows.settings.user_setting.user_class import Ui_Dialog, QDialog

from data_base.test_orm import update_image, update_user, select_User
from data_base.models import User

from functions.circle_image.circle_image import setCircleImage
from functions.settings.settings import load_theme
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
        #TODO user_id, image
        self.user_id = user_id
        self.image = None
        self.__start()
        self.ui.push_button_chose_image.clicked.connect(self.__chose_image)
        self.ui.push_button_save.clicked.connect(self.__save)

    def __start(self):
        user: User = select_User(user_id= self.user_id)
        self.ui.linedit_username.setText(user.username)
        if user.image is not None:
            self.__circle_image(user.image)

    def __chose_image(self):
        filedialog = QFileDialog()
        # тут доделать параметры
        self.image = filedialog.getOpenFileName(caption='Выбрать файл'
                                                    )

        if self.image != ('', ''):
            self.__circle_image(self.image[0])

    def __save(self):
        self.__save_image()
        self.__save_user()

    def __save_image(self):
        if self.image is not None:
            img = Image.open(self.image[0])
            img = img.convert('RGB')
            path = f'Data\\Data_base\\image\\{os.path.splitext(os.path.basename(self.image[0]))[0]}.jpg'
            img.save(path, 'JPEG', quality=80)

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

        if all(
            empty := (self.ui.linedit_password.text() != ''),
            old_password := (self.ui.linedit_password.text() != user.password),
            (check_password := check_password_strength(self.ui.linedit_password.text()))[0]
        ):
            password= self.ui.linedit_password.text()
            self.ui.label_walidation_password.setText(
                'Пароль сохронён'
            )
        else:
            if not old_password:
                self.ui.label_walidation_password.setText(
                "<p style='color: red'>Укажите новый пароль</p>"
            )
            elif not check_password[0] and empty:
                self.ui.label_walidation_password.setText(
                    f"<p style='color: red'>{check_password[1]}</p>"
                )

        if any(_obj is None for _obj in (user_name, password)):
            update_user(
                user_id= self.user_id,
                username= user_name,
                password= password
            )

    def __circle_image(self, image_path):
        target_pixmap = setCircleImage(
            image_path,
            self.ui.label_image.size().height()
        )
        self.ui.label_image.setPixmap(target_pixmap)
