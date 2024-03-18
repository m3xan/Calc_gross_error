"""
Модуль с ядром для праллельного сохронения данных из эксель
"""
from PySide6.QtCore import QThread

from functions.excel import excel

class SaveThread(QThread):
    """
    Ядро для праллельного сохронить данных из эксель
    """
    def __init__(self, path: str, new_dict: dict):
        super().__init__()
        self.path = path
        self.new_dict = new_dict

    def run(self):
        excel.save_result_calc_excel(self.path, self.new_dict)
