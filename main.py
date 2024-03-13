"""
Главный запускаемый файл проекта
"""
import sys

from PySide6.QtWidgets import QApplication

from window.second_windows.authorization_window.authorization_window import AuthorizationWindow

def main() -> None:
    """
    Открывает приложение
    """
    app = QApplication(sys.orig_argv)
    window = AuthorizationWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
