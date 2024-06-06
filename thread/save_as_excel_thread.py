"""
Модуль с ядром для праллельного сохроненть как данных из эксель
"""
from PySide6.QtCore import QThread

from functions.excel.excel import Excel
from data_class.data import Data

class SaveAsThread(QThread):
    """
    Ядро для праллельного сохронить как данных из эксель
    """
    def __init__(self, path: str, data: Data):
        super().__init__()
        self.path = path
        self.data = data

    def run(self):
        saver = Excel.FileSaver()
        saver.data = self.data
        saver.save_file(self.path)
