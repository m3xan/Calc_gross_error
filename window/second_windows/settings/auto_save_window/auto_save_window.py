"""
Переделать логику
"""

from window.second_windows.settings.auto_save_window.auto_save_class import Ui_DialogAutoSave, QDialog
from window.data_class_for_window.dataclass import BaseDataclassWindows

from settings.settings import load_theme, load_category_json, save_data_json

class AutoSaveWindow(QDialog):
    """
    Класс окна настроек автосохронения
    """
    def __init__(self, user_id):
        super().__init__()
        self.ui = Ui_DialogAutoSave()
        self.ui.setupUi(self)

        self.state = BaseDataclassWindows(
            theme= load_theme(self)
        )
        self.user_id = user_id

        self.__set_value()
        self.ui.push_button_save.clicked.connect(self.save_setting)

        # checkBox
        self.ui.checkBox.toggled.connect(self.checkBox_toggled)

    def save_setting(self):
        if self.ui.checkBox.isChecked():
            data = {"switched": True, "time": self.ui.spinBox.value() * 60000}
        else:
            data  = {"switched": False}
        save_data_json('auto_save', None , data, user_id= self.user_id)
        return True

    def checkBox_toggled(self):
        self.ui.spinBox.setEnabled(self.ui.checkBox.isChecked())

    def __set_value(self):
        try:
            self.ui.checkBox.setChecked(load_category_json('auto_save', self.user_id)['switched'])
            self.ui.spinBox.setEnabled(load_category_json('auto_save', self.user_id)['switched'])
            if load_category_json('auto_save', self.user_id)['switched']:
                self.ui.spinBox.setValue(load_category_json('auto_save', self.user_id)['time']/60000)
        except TypeError:
            self.ui.checkBox.setEnabled(True)
            self.ui.spinBox.setDisabled(True)
