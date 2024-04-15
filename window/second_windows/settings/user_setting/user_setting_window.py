"""
Переделать логику
"""

import os

from PySide6.QtWidgets import QFileDialog
from PIL import Image

from window.second_windows.settings.user_setting.user_class import Ui_Dialog
from window.abstract_model.models import AbstractDialog

from data_base.user.user_models import User

from functions.circle_image.circle_image import ImageChanger
from functions.walidation.walid_password import check_password_strength

from global_param import STANDART_IMAGE

class UserSettingsDialog(AbstractDialog):
    """
    Класс окна настроек интерфейса
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.change_theme()
        #TODO image
        self.image = None
        self.__start()
        self.ui.push_button_chose_image.clicked.connect(self.__chose_image)
        self.ui.push_button_save.clicked.connect(self.__save)

    def __start(self):
        user: User = self.user_db.select_user()
        self.ui.linedit_username.setText(user.username)
        if user.image is not None and os.path.isfile(user.image):
            self.__circle_image(user.image)
        else:
            self.__circle_image(
                STANDART_IMAGE
            )

    def __chose_image(self):
        filedialog = QFileDialog()
        self.image = filedialog.getOpenFileName(
            caption='Выбрать файл',
            filter= 'Image File (*.png;*.jpg;*.gif;*.svg)'
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

            self.user_db.update_image(path)
            return True
        return None

    def __save_user(self):
        user: User = self.user_db.select_user()
        user_name = None
        password = None
        if self.ui.linedit_username.text() != user.username:
            user_name = self.ui.linedit_username.text()

        if all((
            empty := (self.ui.linedit_password.text() != ''),
            old_password := (self.ui.linedit_password.text() != user.password),
            (check_password := check_password_strength(self.ui.linedit_password.text()))[0]
        )):
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

        if any(
            _obj is not None for _obj in (user_name, password)
        ):
            self.user_db.update_user(
                username= user_name,
                password= password
            )

    def __circle_image(self, image_path):
        target_pixmap = ImageChanger(image_path).circle_image(
            self.ui.label_image.size().height()
        )
        self.ui.label_image.setPixmap(target_pixmap)
