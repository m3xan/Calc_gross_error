"""
Переделать логику
"""

from functions import logger
from functions.settings.pydantic_model import AutoSave, GraphSettings
from window.abstract_model.models import AbstractDialog
from window.second_windows.settings.auto_save_window.auto_save_class import Ui_DialogAutoSave

class AutoSaveWindow(AbstractDialog):
    """
    Класс окна настроек автосохронения
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogAutoSave()
        self.ui.setupUi(self)

        self.change_theme()
        self.__set_value()
        self.ui.push_button_save.clicked.connect(self.save_setting)

        self.ui.check_box_auto_save.toggled.connect(self.__check_box_auto_save_toggled)
        self.ui.push_button_esc.clicked.connect(self.reject)

    @logger.debug
    def save_setting(self):
        """
        Заглушка
        """
        settings = self.settings.load_json()
        settings.save_user_name = self.ui.check_box_save_user_name.isChecked()
        settings.graph_settinsgs = GraphSettings(
            window_size= self.ui.spin_box_window_size.value()
        )
        settings.auto_save = AutoSave(
            switched= self.ui.check_box_auto_save.isChecked(),
            time= self.ui.spinBox.value() * 60000
        )
        self.settings.save_json(settings)
        self.change_theme()
        return True

    def __check_box_auto_save_toggled(self):
        self.ui.spinBox.setEnabled(self.ui.check_box_auto_save.isChecked())

    @logger.info
    def __set_value(self):
        settings = self.settings.load_json()

        self.ui.check_box_auto_save.setChecked(
            settings.auto_save.switched
        )
        self.ui.spinBox.setEnabled(
            settings.auto_save.switched
        )
        self.ui.spinBox.setValue(
            settings.auto_save.time / 60000
        )
        self.ui.check_box_save_user_name.setChecked(
            settings.save_user_name
        )
        self.ui.spin_box_window_size.setValue(
            settings.graph_settinsgs.window_size
        )
        return True
