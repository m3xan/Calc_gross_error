"""
Главный запускаемый файл проекта
"""
import sys
import logging

from window.application import QApplicationWithLogging
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
    except FileNotFoundError as err:
        raise err
    except Exception as err:
        logging.critical(err, exc_info= True)
        raise err

if __name__ == "__main__":
    main()
    print(12)
