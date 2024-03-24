
from PySide6.QtCore import Slot

from window.main_window.main_window import MainWindow
from window.second_windows.authorization_window.authorization_window_class import Ui_AuthorizationWindow
from window.second_windows.authorization_window.internal_window.login.login_window import InternalAutorizationWindow
from window.second_windows.authorization_window.internal_window.registration.registration_window import InternalRegistrationWindow

from window.abstract_model.models import AbstractWindow

from functions.new_file.check_file import check_all_file

class AuthorizationWindow(AbstractWindow):
    """autorization window"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_AuthorizationWindow()
        self.ui.setupUi(self)
        self.main_window = None

        self.aut_win = InternalAutorizationWindow()
        self.aut_win.registrarion.connect(self.__set_window)
        self.aut_win.windowThemeChanged.connect(self.__open_mainwindow)

        self.reg_win = InternalRegistrationWindow()
        self.reg_win.autorisation.connect(self.__set_window)
        self.reg_win.windowThemeChanged.connect(self.__open_mainwindow)

        self.ui.horizontalLayout.addWidget(self.aut_win)
        self.ui.horizontalLayout.addWidget(self.reg_win)
        self.reg_win.setVisible(False)

    @Slot(bool)
    def __set_window(self, signall: bool):
        if signall:
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

    @Slot(int)
    def __open_mainwindow(self, signall: int):
        if check_all_file():
            self.main_window = MainWindow(signall)
            self.main_window.show()
            self.deleteLater()

    def __str__(self) -> str:
        _reg = self.reg_win.isVisible()
        _aut = self.aut_win.isVisible()
        return f'visible registration window {_reg}, visible autofication window {_aut}'
