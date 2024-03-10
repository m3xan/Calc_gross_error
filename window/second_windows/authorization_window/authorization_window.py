

from window.main_window.main_window import MainWindow
from window.second_windows.authorization_window.authorization_window_class import Ui_AuthorizationWindow, QMainWindow
from window.second_windows.authorization_window.internal_window.login.login_window import InternalAutorizationWindow
from window.second_windows.authorization_window.internal_window.registration.registration_window import InternalRegistrationWindow

class AuthorizationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AuthorizationWindow()
        self.ui.setupUi(self)

        self.aut_win = InternalAutorizationWindow()
        self.aut_win.registrarion.connect(self.set_AutWindow)
        self.aut_win.fin_aut.connect(self.open_main_window)

        self.reg_win = InternalRegistrationWindow()
        self.reg_win.autorisation.connect(self.set_ReGWindow)
        self.reg_win.reg_finish.connect(self.open_main_window)

        self.ui.horizontalLayout.addWidget(self.aut_win)
        self.ui.horizontalLayout.addWidget(self.reg_win)
        self.reg_win.setVisible(False)

    def set_AutWindow(self, signall):
        if signall:
            self.setWindowTitle('Регистрация')
            self.reg_win.setVisible(True)
            self.aut_win.setVisible(False)

    def set_ReGWindow(self, signall):
        if signall:
            self.setWindowTitle('Авторизация')
            self.reg_win.setVisible(False)
            self.aut_win.setVisible(True)

    def open_main_window(self, signall):
        self.main_window = MainWindow(signall)
        self.main_window.show()
        self.deleteLater()
