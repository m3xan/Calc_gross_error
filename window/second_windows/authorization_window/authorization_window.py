
from PySide6.QtCore import Slot

from window.abstract_model.models import AbstractWindow
from window.main_window.main_window import MainWindow
from window.second_windows.authorization_window.authorization_window_class import Ui_AuthorizationWindow
from window.second_windows.authorization_window.internal_window.login.login_window import InternalAutorizationWindow
from window.second_windows.authorization_window.internal_window.registration.registration_window import InternalRegistrationWindow
from window.message_window.error_window import ErroWindow

from functions.new_file.check_file import FileChecker

from global_param import FILE_PATHS

class AuthorizationWindow(AbstractWindow):
    """autorization window"""
    main_window = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_AuthorizationWindow()
        self.ui.setupUi(self)

        self.reg_win = InternalRegistrationWindow()
        self.reg_win.autorisation.connect(self.__set_window)
        self.reg_win.open_mainwindow.connect(self.__open_mainwindow)

        self.aut_win = InternalAutorizationWindow()
        self.aut_win.registrarion.connect(self.__set_window)
        self.aut_win.open_mainwindow.connect(self.__open_mainwindow)

        self.ui.horizontalLayout.addWidget(self.aut_win)
        self.ui.horizontalLayout.addWidget(self.reg_win)
        self.reg_win.setVisible(False)

    @Slot(bool)
    def __set_window(self):
        if self.aut_win.isVisible():
            self.reg_win.setVisible(True)
            self.aut_win.setVisible(False)
            self.setWindowTitle('Регистрация')
            return True
        if self.reg_win.isVisible():
            self.reg_win.setVisible(False)
            self.aut_win.setVisible(True)
            self.setWindowTitle('Авторизация')
            return True
        return None

    @Slot()
    def __open_mainwindow(self):
        if FileChecker(FILE_PATHS).check_all():
            self.main_window = MainWindow()
        else:
            self.main_window = ErroWindow()
            self.main_window.set_message('All file not found')
        self.main_window.show()
        self.deleteLater()

    def __str__(self) -> str:
        _reg = self.reg_win.isVisible()
        _aut = self.aut_win.isVisible()
        return f'visible registration window {_reg}, visible autofication window {_aut}'
