"""
Модуль с ядром для праллельного считывания данных из эксель
"""

from typing import overload

from PySide6.QtCore import QThread, Signal

from functions.excel import excel
from data_base.user.user_hanler import DatabaseUsersHandler

from data_class.data import Data

class ReadThread(QThread):
    """
    Ядро для праллельного считывания данных
    """
    read_signal = Signal(Data)

    @overload
    def __init__(self, path: str) -> None: ...
    @overload
    def __init__(self) -> None: ...

    def __init__(self, path = None):
        super().__init__()
        self.path = path

    def run(self):
        if self.path:
            self.read_signal.emit(excel.read_file_excel(self.path))
        else:
            user_db = DatabaseUsersHandler()
            self.read_signal.emit(user_db.select_calculation())
