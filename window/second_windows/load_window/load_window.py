"""
заглушка
"""
from PySide6.QtWidgets import QDialog

from window.second_windows.load_window.load_window_class import Ui_Dialog
from window.data_class_for_window.dataclass import BaseDataclassWindows

from functions.settings.settings import JsonSettings

class LoadDialog(QDialog):
    """
    Класс окна которое открывается при загрузки
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.state = BaseDataclassWindows(
            theme= JsonSettings().load_theme(self)
        )
