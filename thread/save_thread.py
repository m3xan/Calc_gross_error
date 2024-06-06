"""
Модуль с ядром для праллельного сохронения данных
"""

from typing import overload

from PySide6.QtCore import QThread, Signal

from functions.excel.excel import Excel
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

    def __init__(self, data, path= None):
        super().__init__()
        self.path = path
        self.data = data

    def run(self):
        if self.path:
            saver = Excel.FileSaver()
            saver.data = self.data
            data = saver.save_file(self.path)
        else:
            data = DatabaseUsersHandler().save_data(self.data)
        self.saved.emit(data)
