"""
заглушка
"""
from PySide6.QtCore import Signal, Slot

from window.data_class_for_window.dataclass import DataclassUserSettingsDialog
from window.abstract_model.models import AbstractWindow

from functions import logger
from functions.walidation.walidate_password import UserWalidater
from functions.new_file.create_settings import create_settngs

from .registration_window_class import Ui_Registration

class InternalRegistrationWindow(AbstractWindow):
    """
    заглушка
    """
    autorisation: Signal = Signal()
    open_mainwindow:Signal = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Registration()
        self.ui.setupUi(self)

        self.state = DataclassUserSettingsDialog()
        self.change_theme()

        self.ui.line_edit_password_main.editingFinished.connect(self.__check_password)
        self.ui.line_edit_login.editingFinished.connect(self.__check_login)
        self.ui.push_button_fin_registration.clicked.connect(self.__fin_registration)
        self.ui.push_button_login.clicked.connect(self.__set_login_window)
        self.ui.line_edit_password_check.setEnabled(False)

    @Slot()
    @logger.debug
    def __check_login(self):
        # TODO check login
        if self.ui.line_edit_login.text() == '':
            return None

        if self.user_db.select_image(self.ui.line_edit_login.text()) is not None:
            self.ui.label_error.setText('Данный логин уже занят')
            return True

        if len(self.ui.line_edit_login.text()) < 5:
            self.ui.label_error.setText('Логин должен быти не менее 5 символов')
            return True

        self.state.check_login_user = True
        self.ui.label_error.clear()
        return f'{self.state.check_login_user=}'

    @Slot()
    @logger.debug
    def __check_password(self):
        if (password_chesk := UserWalidater.check_password(
            self.ui.line_edit_password_main.text()
        ))[0]:
            self.ui.line_edit_password_check.setEnabled(True)
            self.state.check_password_user = True
        self.ui.label_error.setText(password_chesk[1])
        return f'{self.state.check_password_user=}'

    @Slot()
    def __fin_registration(self):
        if all((
            self.ui.line_edit_login.text() != '',
            self.ui.line_edit_password_main.text() == self.ui.line_edit_password_check.text(),
            self.state.check_password_user,
            self.state.check_login_user
        )):
            self.user_db.add_user(
                self.ui.line_edit_login.text(),
                self.ui.line_edit_password_main.text()
            )
            new_user_id = self.user_db.autorisation(
                self.ui.line_edit_login.text(),
                self.ui.line_edit_password_main.text()
            )
            create_settngs(new_user_id)
            self.user_db.set_id(new_user_id)
            self.open_mainwindow.emit()

    @Slot()
    def __set_login_window(self):
        self.autorisation.emit()
