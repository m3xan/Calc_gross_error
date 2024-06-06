
from abc import ABC
import ast
import logging
from typing import overload
import os

import pandas as pd

from data_class.data import Data


class FileKeeper(ABC):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, path: str) -> None: ...

    def __init__(self, path_ = None) -> None:
        self.path = path_

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path_: str):
        #test
        try:
            if os.path.isfile(path_):
                self.__path = path_
            else:
                with open(path_, 'w', encoding='utf-8'):
                    ...
                self.__path = path_
        except TypeError:
            self.__path = None
        except OSError:
            self.__path = None


class Excel:
    version = '0.0.0.1'

    class FileReader(FileKeeper):
        def __init__(self, path_: str = None) -> None:
            super().__init__(path_)
            self.data = Data()

        def read_file(self):
            """
            Читает файл эксель и возвращает список строк.
            Returns:
                Data
            """
            df = pd.read_excel(self.path)
            index_name = 0
            for name in df:
                insert_name = index_name, name
                self.data.append_name(insert_name)
                index = 0
                for values in df[name]:
                    match index:
                        case 0:
                            values = ast.literal_eval(values)
                            for value in values:
                                self.data.append_value(insert_name, float(value))
                        case 1:
                            if '1' in values:
                                self.data.append_method(insert_name, 1)
                        case 2:
                            values = ast.literal_eval(values)
                            for answer in values:
                                self.data.append_answer(insert_name, float(answer))
                    index += 1
                index_name += 1
            logging.debug('read excel file')
            return self.data

    class FileSaver(FileKeeper):

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, data_: Data):
            if isinstance(data_, Data):
                self.__data = data_

        def save_file(self, path_):
            df = self.__data.to_DataFrame()
            # TODO доделть с методом
            df['method'] = df['method'].apply(
                lambda x: 'Не подсчитано' if not x else f'методом "{x}"'
            )
            df = df.T
            df.to_excel(path_, index= False, header= False, sheet_name= 'Измерения')
            logging.debug('save excel file')
            self.__data.metadate_clear()
            logging.debug('metadate clear')
            return self.__data
