"""
Заглушка
"""
from PySide6.QtWidgets import QDialog

from window.second_windows.about_window.about_window_class import Ui_Dialog
from window.data_class_for_window.dataclass import BaseDataclassWindows
from window.second_windows.about_window.snake_game import SnakeGame

from functions.settings.settings import load_theme

class AboutDialog(QDialog):
    """
    Класс окна "о нас"
    """
    def __init__(self, user_id):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.user_id = user_id
        self.state = BaseDataclassWindows(
            theme= load_theme(self, user_id)
        )

        self.key_sequence = []
        self.key_sequence_required = ['q', 'w', 'e', 'r', 't', 'y']

    def keyPressEvent(self, event):
        key = event.text()
        if len(self.key_sequence) > 10:
            self.key_sequence.clear()
        self.key_sequence.append(key)
        if self.key_sequence == self.key_sequence_required:
            self.key_sequence.clear()
            self.show_game()

    def show_game(self):
        window = SnakeGame(self.user_id)
        window.exec()
