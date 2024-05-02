"""
хранить датаклассы для окон
"""

from dataclasses import dataclass

from PySide6.QtGui import QIcon

from data_class.data import Data

# переделать что бы были изначальные значения или нет

@dataclass
class DataclassAddWindow():
    """
    settings for AddDialog
    """
    save_data_mode: bool | None
    change_mode: bool | None

@dataclass
class DataclassMainWindow(DataclassAddWindow):
    """
    settings for MainWindow
    """
    active_mod: str | None
    save_data_mode: bool | None
    data: Data | None
    excel_path: str | None
    add_mod: bool | None
    auto_save_time: dict
    clearance_level: int

@dataclass
class DataclassSettingsWindow():
    """
    settings for SettingDialog
    """
    save_data_mode: bool

@dataclass
class DataclassUserSettingsDialog():
    check_login_user: bool = False
    check_password_user: bool = False

@dataclass
class DataclassAutWindow():
    close_eye: QIcon
    open_eye: QIcon
