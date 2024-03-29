
from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6.QtCore import Signal

from functions.settings.settings import load_theme

class AbstractWindow(QMainWindow):
    windowThemeChanged: Signal = Signal(int)

    def change_theme(self, user_id: int):
        """change theme on window and do signall ThemeChange"""
        self.windowThemeChanged.emit(user_id)
        return load_theme(self, user_id)

class AbstractDialog(QDialog):
    windowThemeChanged: Signal = Signal(int)

    def change_theme(self, user_id: int):
        """change theme on window and do signall ThemeChange"""
        self.windowThemeChanged.emit(user_id)
        return load_theme(self, user_id)
