"""
Переделать логику
"""

from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Slot

from window.abstract_model.models import AbstractDialog
from window.data_class_for_window.dataclass import DataclassSettingsDialog
from window.second_windows.settings.main_settings.settings_class import Ui_Dialog
from window.second_windows.settings.auto_save_window.auto_save_window import AutoSaveWindow
from window.second_windows.settings.setting_window.settings_window import SettingDialog
from window.second_windows.settings.user_setting.user_setting_window import UserSettingsDialog

class SettingsDialog(AbstractDialog):
    """
    Класс окна настроек интерфейса
    """
    def __init__(self, user_id: int):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.state = DataclassSettingsDialog(
            theme= self.change_theme(user_id),
            user_id= user_id
        )

        self.__init_reaction()
        self.__start()


    def __init_reaction(self):
        self.ui.push_button_main.clicked.connect(self.set_main_setting)
        self.ui.push_button_profile.clicked.connect(self.set_profile_setting)
        self.ui.push_button_setting_window.clicked.connect(self.set_widow_setting)

    def __start(self):
        windows = AutoSaveWindow(self.state.user_id)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(windows)
        self.ui.widget.setLayout(self.layout)

    def set_main_setting(self):
        self.__clear()
        windows = AutoSaveWindow(self.state.user_id)
        self.layout.addWidget(windows)

    def set_profile_setting(self):
        self.__clear()
        windows = UserSettingsDialog(self.state.user_id)
        self.layout.addWidget(windows)

    def set_widow_setting(self):
        self.__clear()
        setting_window = SettingDialog(self.state.user_id)
        setting_window.windowThemeChanged.connect(self.send_signal_to_MainWindow)
        self.layout.addWidget(setting_window)

    @Slot(int)
    def send_signal_to_MainWindow(self, signal):
        self.state.theme = self.change_theme(signal)

    def __clear(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().deleteLater()
