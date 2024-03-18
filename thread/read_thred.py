"""
Модуль с ядром для праллельного считывания данных из эксель
"""

from PySide6.QtCore import QThread, Signal

from functions.excel import excel

class ReadThread(QThread):
    """
    Ядро для праллельного считывания данных из эксель 
    """
    read_excel_signal = Signal(str)
    def  __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        self.read_excel_signal.emit(str(excel.read_file_excel(self.path)))
