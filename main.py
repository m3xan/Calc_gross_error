"""
Главный запускаемый файл проекта
"""
import sys
import logging

from window.Application import QApplicationWithLogging
from window.second_windows.authorization_window.authorization_window import AuthorizationWindow

def main() -> None:
    """
    Открывает приложение
    """
    # TODO add logging
    try:
        app = QApplicationWithLogging(sys.orig_argv)
        window = AuthorizationWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as err:
        logging.critical(err, exc_info= True)
        raise err

if __name__ == "__main__":
    main()
