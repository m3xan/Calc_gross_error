"""
заглушка
"""

import os
import logging
import concurrent.futures as concur
from typing import overload

class FileChecker:
    """
    заглушка
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, file_path: str) -> None: ...

    def __init__(self, file_path = None) ->  None:
        if file_path is not None:
            self.set_file_path(file_path)
        else:
            self._file_path = None

    def set_file_path(self, file_path: list[str, ]) -> bool:
        """
        заглушка
        """
        if all((
            isinstance(file_path, list),
            (isinstance(file, str) for file in file_path)
        )):
            self._file_path = file_path
            return True
        return False

    def get_file_path(self):
        return self._file_path

    def __check_file(self, file_name: str) -> bool:
        """
        заглушка
        """
        file_exists = os.path.exists(file_name)
        logging.info(f'File {file_name} {'found' if file_exists else 'not found'}')
        return file_exists

    def check_all(self) -> bool:
        """
        True когда все файлы для работы найдены.
        False когда какой либо файл не найден.
        """
        if self._file_path is not None:
            with concur.ThreadPoolExecutor() as executor:
                return all(executor.map(self.__check_file, self._file_path))
        return False
