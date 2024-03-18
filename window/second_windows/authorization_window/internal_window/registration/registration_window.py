
from PySide6.QtCore import Signal

from window.second_windows.authorization_window.internal_window.registration.registration_window_class import Ui_Registration, QMainWindow
from window.data_class_for_window.dataclass import BaseDataclassWindows

from data_base.test_orm import autorisation
from data_base.test_orm import select_image, add_user

from functions.settings.settings import load_theme

from functions.new_file.create_settings import create_settngs
from functions.walidation.walid_password import check_password_strength

class InternalRegistrationWindow(QMainWindow):
    autorisation: Signal = Signal(bool)
    reg_finish: Signal = Signal(int)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Registration()
        self.ui.setupUi(self)

        self.state = BaseDataclassWindows(
            theme= load_theme(self),
        )
        self.check_login_user = False
        self.check_password_user = False
        self.ui.line_edit_password_main.editingFinished.connect(self.check_password)
        self.ui.line_edit_login.editingFinished.connect(self.check_login)
        self.ui.push_button_fin_registration.clicked.connect(self.__fin_registration)
        self.ui.push_button_login.clicked.connect(self.to_login)
        self.ui.line_edit_password_check.setEnabled(False)

    def check_login(self):
        if self.ui.line_edit_login.text() == '':
            pass
        elif select_image(input_username= self.ui.line_edit_login.text()) is not None:
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

    def check_password(self):
        password_chesk = check_password_strength(self.ui.line_edit_password_main.text())
        if password_chesk[0]:
            self.ui.line_edit_password_check.setEnabled(True)
            self.check_password_user = True
        self.ui.label_error.setText(password_chesk[1])

    def __fin_registration(self):

        rigth_pass = self.ui.line_edit_password_main.text() == self.ui.line_edit_password_check.text()
        if self.ui.line_edit_login.text() != '' and rigth_pass and self.check_password_user and self.check_login_user:
            add_user(
                username= self.ui.line_edit_login.text(),
                password= self.ui.line_edit_password_main.text()
            )
            new_user_id = autorisation(self.ui.line_edit_login.text(), self.ui.line_edit_password_main.text())
            create_settngs(new_user_id)
            self.reg_finish.emit(new_user_id)

    def to_login(self):
        self.autorisation.emit(True)
