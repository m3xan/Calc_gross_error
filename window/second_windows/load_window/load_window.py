"""
заглушка
"""

from window.abstract_model.models import AbstractDialog

from .load_window_class import Ui_Dialog

class LoadDialog(AbstractDialog):
    """
    Класс окна которое открывается при загрузки
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.change_theme()
