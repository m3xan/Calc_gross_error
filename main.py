"""
Главный запускаемый файл проекта
"""
import sys
import logging

from window.application import QApplicationWithLogging
from window.second_windows.authorization_window.authorization_window import AuthorizationWindow

class Programm:
    """
    class storing main (method)
    """
    def main(self) -> None:
        """
        Открывает приложение
        """
        try:
            self.__start()
        except FileNotFoundError as err:
            raise err
        except Exception as err:
            logging.critical(err, exc_info= True)
            raise err

    def __start(self):
        app = QApplicationWithLogging(sys.orig_argv)
        window = AuthorizationWindow()
        window.show()
        sys.exit(app.exec())

if __name__ == '__main__':
    Programm().main()
