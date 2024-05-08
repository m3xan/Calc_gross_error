"""
Модуль с ядром для праллельного сохронения данных
"""

from typing import overload

from PySide6.QtCore import QThread, Signal

from functions.excel import excel

from data_base.user.user_hanler import DatabaseUsersHandler
from data_class.data import Data


class SaveThread(QThread):
    """
    Ядро для праллельного сохронить данных
    """
    saved: Signal = Signal(Data)

    @overload
    def __init__(self, data: Data, path: str): ...
    @overload
    def __init__(self, data: Data): ...

    def __init__(self, data, path = None):
        super().__init__()
        self.path = path
        self.data = data

    def run(self):
        if self.path is None:
            data = excel.save_result_calc_excel(self.path, self.data)
        else:
            data = DatabaseUsersHandler().save_data(self.data)
        self.saved.emit(data)
