
from typing import overload

from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6.QtCore import Signal

from functions.settings.settings import JsonSettings
from data_base.user_hanler import DatabaseUsersHandler

class AbstractThemeChanger:
    """
    abctarct class stores method change_theme
    and param windowThemeChanged type Signal
    have JsonSettings and DatabaseUsersHandler
    """
    windowThemeChanged: Signal = Signal(int)
    settings = JsonSettings()
    user_db = DatabaseUsersHandler()

    @overload
    def change_theme(self) -> str | None: ...
    @overload
    def change_theme(self, user_id: int) -> str | None: ...

    def change_theme(self, user_id: int = None):
        """change theme on window and do signall ThemeChange"""
        if user_id is None:
            self.windowThemeChanged.emit(self.settings.get_user_id())
        else:
            self.windowThemeChanged.emit(user_id)
        return self.__load_theme(user_id)

    def __load_theme(self, user_id: int | None):
        if user_id is not None:
            self.settings.set_user_id(user_id)
            return self.settings.load_theme(self)
        return self.settings.load_theme(self)

class AbstractWindow(QMainWindow, AbstractThemeChanger): """заглушка"""

class AbstractDialog(QDialog, AbstractThemeChanger): """заглушка"""
