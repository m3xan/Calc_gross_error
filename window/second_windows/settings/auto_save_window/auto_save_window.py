"""
Переделать логику
"""
import logging

from functions.settings.pydantic_model import AutoSave
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

        self.ui.check_box_auto_save.toggled.connect(self.check_box_auto_save_toggled)
        self.ui.push_button_esc.clicked.connect(self.reject)

    def save_setting(self):
        """
        Заглушка
        """
        settings = self.settings.load_json()
        settings.save_user_name = self.ui.check_box_save_user_name.isChecked()
        settings.auto_save = AutoSave(
            switched= self.ui.check_box_auto_save.isChecked(),
            time= self.ui.spinBox.value() * 60000
        )
        self.settings.save_json(settings)
        return True

    def check_box_auto_save_toggled(self):
        self.ui.spinBox.setEnabled(self.ui.check_box_auto_save.isChecked())

    def __set_value(self):
        try:
            auto_save = self.settings.load_auto_save()
            self.ui.check_box_auto_save.setChecked(
                auto_save.switched
            )
            self.ui.spinBox.setEnabled(
                auto_save.switched
            )
            self.ui.check_box_save_user_name.setChecked(
                self.settings.load_json().save_user_name
            )
            if auto_save:
                self.ui.spinBox.setValue(auto_save.time/60000)
        except TypeError as err:
            logging.error(err, exc_info=True)
            self.ui.check_box_auto_save.setEnabled(True)
            self.ui.spinBox.setDisabled(True)
