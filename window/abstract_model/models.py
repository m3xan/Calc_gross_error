

from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6.QtCore import Signal

from settings.settings import load_theme

class AbstractWindow(QMainWindow):
    windowThemeChanged: Signal = Signal(int)

    def change_theme(self, user_id):
        load_theme(self, user_id)
        self.windowThemeChanged.emit(user_id)

class AbstractDialog(QDialog):
    dialogThemeChanged: Signal = Signal(int)

    def change_theme(self, user_id):
        load_theme(self, user_id)
        self.dialogThemeChanged.emit(user_id)
