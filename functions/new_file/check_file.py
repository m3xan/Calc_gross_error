"""
заглушка
"""

import os
import logging
import concurrent.futures as concur
from typing import overload

from functions import logger
from global_param import IterVar

class FileChecker:
    """
    заглушка
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, file_path: IterVar) -> None: ...

    def __init__(self, file_path_ = None) ->  None:
        if file_path_ is not None:
            self.file_path = file_path_
        else:
            self._file_path = None

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: IterVar) -> bool:
        try:
            if issubclass(file_path, IterVar):
                self._file_path = file_path()
                return True
        except ValueError:
            return False
        except Exception as err:
            logging.critical(err, exc_info= True)
            raise err

    def __check_file(self, file_name: str) -> bool:
        file_exists = os.path.exists(file_name)
        logging.info(f'File {file_name} {'found' if file_exists else 'not found'}')
        return file_exists

    @logger.info
    def check_all(self) -> bool:
        """
        True когда все файлы для работы найдены.
        False когда какой либо файл не найден.
        """
        if self._file_path is not None:
            with concur.ThreadPoolExecutor() as executor:
                return all(executor.map(self.__check_file, self._file_path))
        return False
