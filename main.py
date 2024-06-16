"""
Главный запускаемый файл проекта
"""
import sys
import logging

from window.application import QApplicationWithLogging
from window.second_windows.authorization_window.authorization_window import AuthorizationWindow
from window.message_window.error_window import ErroWindow

from functions.new_file.check_file import FileChecker

from global_param import CriticalFilePath

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

    @staticmethod
    def __start():
        app = QApplicationWithLogging(sys.orig_argv)
        if FileChecker(CriticalFilePath).check_all():
            window = AuthorizationWindow()
        else:
            window = ErroWindow()
            window.set_message('Critical file not found')
        window.show()
        sys.exit(app.exec())

if __name__ == '__main__':
    Programm().main()
