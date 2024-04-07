"""
Переделать логику
"""
import logging

from PySide6.QtWidgets import QHBoxLayout, QLabel, QComboBox, QSizePolicy
from PySide6.QtCore import Slot

from window.abstract_model.models import AbstractDialog
from window.second_windows.settings.setting_window.settings_window_class import Ui_Dialog
from window.data_class_for_window.dataclass import BaseDataclassWindows

from functions.settings.settings import JsonSettings

class SettingDialog(AbstractDialog):
    """
    Класс окна настроек интерфейса
    """
    def __init__(self, user_id):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.settings = JsonSettings()
        self.state = BaseDataclassWindows(
            theme= self.change_theme(user_id)
        )
        self.user_id = user_id

        self.start()

        # push_button
        self.ui.push_button_save.clicked.connect(self.__push_button_save_clicked)
        self.ui.push_button_apply.clicked.connect(self.__push_button_apply)

    @Slot()
    def __push_button_save_clicked(self):
        self.__save()

    @Slot()
    def __push_button_apply(self):
        self.__save()
        self.state.theme= self.change_theme(self.user_id)

    def __save(self):
        for i in self.comdo_box:

            name = i.currentData()[0]
            data = i.currentData()[1]

            self.settings.save_data_json('window', data, name)
        logging.info('save_theme')

    def start(self):
        self.comdo_box: list[QComboBox] = []
        settings = JsonSettings()
        settings.set_user_id('option')
        loading = settings.load_category_json('window')
        for name_property in loading:
            label = QLabel(loading[name_property]['name'])
            variation = settings.load_attribute('window', name_property)['option']
            user_setting = self.settings.load_attribute('window',name_property)

            combo_box = QComboBox()
            self.comdo_box.append(combo_box)
            for variation_name in variation:
                combo_box.addItem(
                    variation_name,
                    (name_property, variation[variation_name])
                )

            sizepolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            combo_box.setSizePolicy(sizepolicy)
            combo_box.setCurrentText(
                self.__find_key(variation, user_setting)
            )

            second_layout = QHBoxLayout()
            second_layout.addWidget(label)
            second_layout.addWidget(combo_box)

            self.ui.verticalLayout_3.addLayout(second_layout)
        settings.set_user_id(self.user_id)

    def __find_key(self, dict_: dict, search_value):
        for key, value in dict_.items():
            if value == search_value:
                return key
        return None
