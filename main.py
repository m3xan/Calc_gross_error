"""
Главный запускаемый файл проекта
"""
import sys

from PySide6.QtWidgets import QApplication

from window.second_windows.authorization_window.authorization_window import AuthorizationWindow
from functions.loger.log import start_loger

def main() -> None:
    """
    Открывает приложение
    """
    # TODO add logging
    start_loger()
    app = QApplication(sys.orig_argv)
    window = AuthorizationWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
