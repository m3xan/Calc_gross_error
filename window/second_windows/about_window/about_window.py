"""
Заглушка
"""

from window.abstract_model.models import AbstractDialog
from window.second_windows.about_window.about_window_class import Ui_Dialog
from window.second_windows.about_window.snake_game import SnakeGame

class AboutDialog(AbstractDialog):
    """
    Класс окна "о нас"
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.change_theme()
        self.key_sequence = []

    def keyPressEvent(self, event):
        key = event.text()
        if len(self.key_sequence) > 10:
            self.key_sequence.clear()
        self.key_sequence.append(key)
        if self.key_sequence == ['q', 'w', 'e', 'r', 't', 'y']:
            self.key_sequence.clear()
            self.show_game()

    def show_game(self):
        window = SnakeGame()
        window.exec()
