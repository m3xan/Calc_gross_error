"""
Модуль с ядром для праллельного сохроненть как данных из эксель
"""
from PySide6.QtCore import QThread

from excel import excel

class SaveAsThread(QThread):
    """
    Ядро для праллельного сохронить как данных из эксель
    """
    def __init__(self, path: str, new_dict: dict, parent=None):
        self.path = path
        self.new_dict = new_dict
        QThread.__init__(self, parent)

    def run(self):
        excel.create_new_file(self.path, self.new_dict)
