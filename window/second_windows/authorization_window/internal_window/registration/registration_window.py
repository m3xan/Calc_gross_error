
from PySide6.QtCore import Signal, Slot

# TODO do module second widow, main window
from window.second_windows.authorization_window.internal_window.registration.registration_window_class import Ui_Registration
from window.data_class_for_window.dataclass import BaseDataclassWindows
from window.abstract_model.models import AbstractWindow

from data_base.user_hanler import DatabaseUsersHandler

from functions.new_file.create_settings import create_settngs
from functions.walidation.walid_password import check_password_strength

class InternalRegistrationWindow(AbstractWindow):
    autorisation: Signal = Signal(bool)
    open_mainwindow:Signal = Signal(int)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Registration()
        self.ui.setupUi(self)

        self.state = BaseDataclassWindows(
            theme= self.change_theme(),
        )
        self.bd = DatabaseUsersHandler()
        self.check_login_user = False
        self.check_password_user = False
        # TODO do dataclass

        self.ui.line_edit_password_main.editingFinished.connect(self.__check_password)
        self.ui.line_edit_login.editingFinished.connect(self.__check_login)
        self.ui.push_button_fin_registration.clicked.connect(self.__fin_registration)
        self.ui.push_button_login.clicked.connect(self.__set_login_window)
        self.ui.line_edit_password_check.setEnabled(False)

    @Slot()
    def __check_login(self):
        # TODO check login
        if self.ui.line_edit_login.text() == '':
            pass
        elif self.bd.select_image(self.ui.line_edit_login.text()) is not None:
            self.ui.label_error.setText(
                'Данный логин уже занят'
            )
        elif len(self.ui.line_edit_login.text()) < 5:
            self.ui.label_error.setText(
                'Логин должен быти не менее 5 символов'
            )
        else:
            self.check_login_user = True
            self.ui.label_error.clear()

    @Slot()
    def __check_password(self):
        if (password_chesk := check_password_strength(
            self.ui.line_edit_password_main.text()
        ))[0]:
            self.ui.line_edit_password_check.setEnabled(True)
            self.check_password_user = True
        self.ui.label_error.setText(password_chesk[1])

    @Slot()
    def __fin_registration(self):
        if all((
            self.ui.line_edit_login.text() != '',
            self.ui.line_edit_password_main.text() == self.ui.line_edit_password_check.text(),
            self.check_password_user,
            self.check_login_user
        )):
            self.bd.add_user(
                self.ui.line_edit_login.text(),
                self.ui.line_edit_password_main.text()
            )
            new_user_id = self.bd.autorisation(
                self.ui.line_edit_login.text(),
                self.ui.line_edit_password_main.text()
            )
            create_settngs(new_user_id)
            self.open_mainwindow.emit(new_user_id)

    @Slot()
    def __set_login_window(self):
        self.autorisation.emit(True)
