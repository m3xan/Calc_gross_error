import logging
import os

from functions.loger.singeton import Singleton

from global_param import FORMAT, SQLLOGER


class Logger(Singleton):

    def start_logger(self):
        """
        init starter loger
        if loger was inited
        doing nothing
        """
        if self._logger is None and self._echo:
            try:
                self.__add_directory()
                self.__init_start_log()
                sqlalchemy_logger = logging.getLogger(SQLLOGER)
                sqlalchemy_logger.propagate = False

                return True
            except Exception as err:
                raise err
        if not self._echo:
            sqlalchemy_logger = logging.getLogger(SQLLOGER)
            sqlalchemy_logger.propagate = False
            return True
        return False

    @staticmethod
    def __add_directory():
        if not os.path.isdir('Data/logging'):
            os.mkdir('Data/logging')

    def __init_start_log(self):
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.INFO)

        file_handler = self.__add_file_logger(
            r'Data\logging\start.log',
            logging.INFO
        )
        console_handler = self.__add_terminal_logger()

        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def __add_file_logger(self, path: str, level: int):
        file_handler = logging.FileHandler(path, encoding='utf-8')
        file_handler.setLevel(level)
        file_formatter = logging.Formatter(FORMAT)
        file_handler.setFormatter(file_formatter)
        return file_handler

    def __add_terminal_logger(self):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter(FORMAT)
        console_handler.setFormatter(console_formatter)
        return console_handler

    def change_logger(self, user_id: int, level: int = logging.ERROR):
        """
        change loger for user
        if level <= 20 start 'sqlalchemy.engine.Engine' loger 
        """
        if self._echo:
            try:
                self._logger.handlers = []
                if level <= 20:
                    logging.getLogger(SQLLOGER).propagate = True
                new_file_handler = self.__add_file_logger(
                    f'Data/logging/{user_id}.log',
                    level
                )
                self._logger.addHandler(new_file_handler)
                self._logger.addHandler(self.__add_terminal_logger())
                self._logger.setLevel(level)
            except Exception as err:
                logging.error(err, exc_info= True)
                raise err
