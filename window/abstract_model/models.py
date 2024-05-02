
from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6.QtCore import Signal

from functions.settings.settings import JsonSettings
from data_base.user.user_hanler import DatabaseUsersHandler

class AbstractThemeChanger:
    """
    abctarct class stores method change_theme
    and param windowThemeChanged type Signal

    have JsonSettings and DatabaseUsersHandler
    """
    windowThemeChanged: Signal = Signal()
    settings = JsonSettings()
    user_db = DatabaseUsersHandler()

    def change_theme(self):
        """change theme on window and do signall ThemeChange"""
        self.windowThemeChanged.emit()
        return self.__load_theme(self.settings.get_user_id())

    def __load_theme(self, user_id: int | None):
        if user_id is not None:
            self.settings.set_user_id(user_id)
            return self.settings.load_theme(self)
        return self.settings.load_theme(self)

class AbstractWindow(QMainWindow, AbstractThemeChanger): """Abstract class for inheritance window"""

class AbstractDialog(QDialog, AbstractThemeChanger): """Abstract class for inheritance dialog"""
