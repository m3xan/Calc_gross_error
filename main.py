"""
Главный запускаемый файл проекта
"""
import logging
import sys

from PySide6.QtWidgets import QApplication

from window.second_windows.authorization_window.authorization_window import AuthorizationWindow

def main() -> None:
    """
    Открывает приложение
    """
    # TODO add logging
    logging.basicConfig(
        filename='Data/logging/user.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
    )
    app = QApplication(sys.orig_argv)
    window = AuthorizationWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
