"""
Переделать логику
"""
import logging

from window.abstract_model.models import AbstractDialog
from window.second_windows.settings.auto_save_window.auto_save_class import Ui_DialogAutoSave
from window.data_class_for_window.dataclass import BaseDataclassWindows

from functions.settings.settings import JsonSettings

class AutoSaveWindow(AbstractDialog):
    """
    Класс окна настроек автосохронения
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogAutoSave()
        self.ui.setupUi(self)

        self.settings = JsonSettings()
        self.state = BaseDataclassWindows(
            theme= self.change_theme()
        )

        self.__set_value()
        self.ui.push_button_save.clicked.connect(self.save_setting)

        # checkBox
        self.ui.checkBox.toggled.connect(self.checkBox_toggled)

    def save_setting(self):
        if self.ui.checkBox.isChecked():
            data = {"switched": True, "time": self.ui.spinBox.value() * 60000}
        else:
            data  = {"switched": False}
        self.settings.save_data_json('auto_save', data)
        return True

    def checkBox_toggled(self):
        self.ui.spinBox.setEnabled(self.ui.checkBox.isChecked())

    def __set_value(self):
        try:
            iseneble = self.settings.load_category_json('auto_save')['switched']
            self.ui.checkBox.setChecked(
                iseneble
            )
            self.ui.spinBox.setEnabled(
                iseneble
            )
            if iseneble:
                self.ui.spinBox.setValue(self.settings.load_category_json('auto_save')['time']/60000)
        except TypeError as err:
            logging.error(err, exc_info=True)
            self.ui.checkBox.setEnabled(True)
            self.ui.spinBox.setDisabled(True)
