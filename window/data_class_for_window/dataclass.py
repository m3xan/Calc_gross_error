"""
хранить датаклассы для окон
"""

from dataclasses import dataclass

from PySide6.QtGui import QIcon

from data_class.data import Data
from functions.settings.pydantic_model import AutoSave

@dataclass(slots= True)
class DataclassAddWindow():
    """
    settings for AddDialog
    """
    save_data_mode: bool | None
    change_mode: bool | None

@dataclass(slots= True)
class DataclassMainWindow(DataclassAddWindow):
    """
    settings for MainWindow
    """
    active_mod: str | None
    save_data_mode: bool | None
    data: Data | None
    excel_path: str | None
    add_mod: bool | None
    auto_save_time: AutoSave
    clearance_level: int

@dataclass(slots= True)
class DataclassSettingsWindow():
    """
    settings for SettingDialog
    """
    save_data_mode: bool

@dataclass(slots= True)
class DataclassUserSettingsDialog():
    """
    заглушка
    """
    check_login_user: bool = False
    check_password_user: bool = False

@dataclass(slots= True)
class DataclassAutWindow():
    """
    заглушка
    """
    close_eye: QIcon
    open_eye: QIcon
