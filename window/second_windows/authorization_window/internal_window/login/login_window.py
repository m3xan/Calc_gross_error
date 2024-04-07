
from PySide6.QtWidgets import QLineEdit, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QIcon

from window.second_windows.authorization_window.internal_window.login.login_window_class import Ui_Autorization
from window.data_class_for_window.dataclass import DataclassAutWindow
from window.abstract_model.models import AbstractWindow

from data_base.test_orm import DatabaseUsersHandler
from data_base.models import User

from functions.settings.settings import JsonSettings
from functions.circle_image.circle_image import ImageChanger

from global_param import STANDART_IMAGE

class InternalAutorizationWindow(AbstractWindow):
    """Внутреннее окно авторизации"""
    registrarion:Signal = Signal(bool)
    open_mainwindow:Signal = Signal(int)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Autorization()
        self.ui.setupUi(self)

        self.state = DataclassAutWindow(
            theme= self.change_theme(self),
            standard_image= STANDART_IMAGE
        )
        self.data_base = DatabaseUsersHandler()

        # TODO add close_eye, open_eye, del self.state.standard_image
        self.close_eye = QIcon(':/button/free-icon-eye-4621498.png')
        self.open_eye = QIcon(':/button/free-icon-open-eye-829117.png')

        self.__init_show_button()
        self.__init_reaction()
        self.__set_image(self.state.standard_image)

    def __set_image(self, image_path):
        target_pixmap = ImageChanger(image_path).setCircleImage(
            desired_size = self.ui.label_image.size().height()
        )
        self.ui.label_image.setPixmap(target_pixmap)

    def __init_show_button(self):
        self.show_button = QPushButton(self)
        self.show_button.setCursor(Qt.PointingHandCursor)
        self.show_button.setStyleSheet("border: none; padding: 0;")
        self.show_button.setIcon(self.open_eye)

        layout = QHBoxLayout(self.ui.line_edit_password)
        layout.setContentsMargins(9, -1, 26, -1)
        layout.addWidget(self.show_button, 0, Qt.AlignRight)

    def __init_reaction(self):
        self.ui.push_button_login.clicked.connect(self.__ckick)
        self.ui.line_edit_login.editingFinished.connect(self.__load_image)
        self.show_button.clicked.connect(self.__password_visibility)
        self.ui.push_button_registration.clicked.connect(self.__set_signall)

    @Slot()
    def __set_signall(self):
        self.registrarion.emit(True)

    @Slot()
    def __password_visibility(self):
        if self.ui.line_edit_password.echoMode() == QLineEdit.Password:
            self.ui.line_edit_password.setEchoMode(QLineEdit.Normal)
            self.show_button.setIcon(self.close_eye)
        else:
            self.ui.line_edit_password.setEchoMode(QLineEdit.Password)
            self.show_button.setIcon(self.open_eye)

    @Slot()
    def __ckick(self):
        if self.ui.line_edit_password.text() != '':
            user_id = self.data_base.autorisation(
                self.ui.line_edit_login.text(),
                self.ui.line_edit_password.text()
            )
            if user_id is not None:
                self.open_mainwindow.emit(user_id)
                return user_id
            return 'Неверный логин или пароль'
        return None

    @Slot()
    def __load_image(self):
        if self.ui.line_edit_login.text() != '':
            user: User = self.data_base.select_image(self.ui.line_edit_login.text())
            if user is not None:
                JsonSettings().set_user_id(user.id)
                self.state.theme = self.change_theme(user.id)
                self.__set_image(user.image)
