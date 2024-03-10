"""
хранить датаклассы для окон
"""

from dataclasses import dataclass

# переделать что бы были изначальные значения или нет
@dataclass
class BaseDataclassWindows:
    """
    Base settings for window
    """
    theme: tuple | None

@dataclass
class DataclassAddWindow(BaseDataclassWindows):
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
    data: dict | None
    excel_path: str | None
    add_mod: bool | None
    auto_save_time: dict
    user_id: int

@dataclass
class DataclassSettingsWindow(BaseDataclassWindows):
    """
    settings for SettingDialog
    """
    save_data_mode: bool

@dataclass
class DataclassAutWindow(BaseDataclassWindows):
    """
    settings for SettingDialog
    """
    standard_image: str

@dataclass
class DataclassSettingsDialog(BaseDataclassWindows):
    """
    settings for SettingDialog
    """
    user_id: int
