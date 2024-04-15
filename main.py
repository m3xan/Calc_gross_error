"""
Главный запускаемый файл проекта
"""
import sys
import logging

from window.application import QApplicationWithLogging
from window.second_windows.authorization_window.authorization_window import AuthorizationWindow
from window.message_window.error_window import ErroWindow

from functions.new_file.check_file import FileChecker

from global_param import CRIRICAL_FILE

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
        if FileChecker(CRIRICAL_FILE).check_all():
            window = AuthorizationWindow()
        else:
            window = ErroWindow()
            window.file_not_faund()
        window.show()
        sys.exit(app.exec())

if __name__ == '__main__':
    Programm().main()
