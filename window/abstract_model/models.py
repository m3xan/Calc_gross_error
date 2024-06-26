
from typing import overload

from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6.QtCore import Signal

from functions.settings.settings import JsonSettings

class AbstractThemeChanger:
    """
    abctarct class stores method change_theme
    and param windowThemeChanged type Signal
    """
    windowThemeChanged: Signal = Signal(int)

    @overload
    def change_theme(self) -> (str | None):
        pass
    @overload
    def change_theme(self, user_id: int) -> (str | None):
        pass

    def change_theme(self, user_id: int | None = None):
        """change theme on window and do signall ThemeChange"""
        self.windowThemeChanged.emit(user_id)
        return self.__load_theme(user_id)

    def __load_theme(self, user_id):
        settings = JsonSettings()
        if user_id is not None:
            settings.set_user_id(user_id)
            return settings.load_theme(self)
        return settings.load_theme(self)

class AbstractWindow(QMainWindow, AbstractThemeChanger): """заглушка"""

class AbstractDialog(QDialog, AbstractThemeChanger): """заглушка"""
