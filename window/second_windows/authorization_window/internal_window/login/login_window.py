
import logging
from PySide6.QtWidgets import QLineEdit, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QIcon

from window.second_windows.authorization_window.internal_window.login.login_window_class import Ui_Autorization
from window.data_class_for_window.dataclass import DataclassAutWindow
from window.abstract_model.models import AbstractWindow

from data_base.user.user_models import User

from functions import logger
from functions.circle_image.circle_image import ImageChanger
from functions.circle_image.image import Image

class InternalAutorizationWindow(AbstractWindow):
    """Внутреннее окно авторизации"""
    registrarion:Signal = Signal()
    open_mainwindow:Signal = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Autorization()
        self.ui.setupUi(self)

        self.state = DataclassAutWindow(
            close_eye= QIcon(':/button/free-icon-eye-4621498.png'),
            open_eye= QIcon(':/button/free-icon-open-eye-829117.png')
        )

        self.__init_show_button()
        self.__init_reaction()

        if loggin := self.settings.load_start():
            self.ui.line_edit_login.setText(loggin)
            self.__load_image()
            logging.debug(f'{loggin=}')
        else:
            self.ui.line_edit_login.setFocusPolicy(Qt.StrongFocus)
            self.__set_image(Image())

    @logger.info
    def __set_image(self, image_path):
        self.ui.label_image.setPixmap(
            ImageChanger(image_path).circle_image(
                self.ui.label_image.size().height()
            )
        )
        return True

    @logger.info
    def __init_show_button(self):
        self.show_button = QPushButton(self)
        self.show_button.setCursor(Qt.PointingHandCursor)
        self.show_button.setStyleSheet("border: none; padding: 0;")
        self.show_button.setIcon(self.state.open_eye)

        layout = QHBoxLayout(self.ui.line_edit_password)
        layout.setContentsMargins(9, -1, 26, -1)
        layout.addWidget(self.show_button, 0, Qt.AlignRight)
        return True

    def __init_reaction(self):
        self.ui.push_button_login.clicked.connect(self.__ckick)
        self.ui.line_edit_login.editingFinished.connect(self.__load_image)
        self.show_button.clicked.connect(self.__password_visibility)
        self.ui.push_button_registration.clicked.connect(self.__set_signall)

    @Slot()
    def __set_signall(self):
        self.registrarion.emit()

    @Slot()
    @logger.info
    def __password_visibility(self):
        if self.ui.line_edit_password.echoMode() == QLineEdit.Password:
            self.ui.line_edit_password.setEchoMode(QLineEdit.Normal)
            self.show_button.setIcon(self.state.close_eye)
        else:
            self.ui.line_edit_password.setEchoMode(QLineEdit.Password)
            self.show_button.setIcon(self.state.open_eye)
        return self.ui.line_edit_password.echoMode()

    @Slot()
    @logger.debug
    def __ckick(self):
        if self.ui.line_edit_password.text() != '':
            user_id = self.user_db.autorisation(
                self.ui.line_edit_login.text(),
                self.ui.line_edit_password.text()
            )
            if user_id:
                self.open_mainwindow.emit()
                return user_id
            return 'Неверный логин или пароль'
        return None

    @Slot()
    @logger.info
    def __load_image(self):
        if self.ui.line_edit_login.text() != '':
            user: User = self.user_db.select_image(self.ui.line_edit_login.text())
            if user:
                self.user_db.set_id(user.id)
                self.settings.set_user_id(user.id)
                self.change_theme()
                self.__set_image(user.image)
                return True
        self.__set_image(Image())
        return None
