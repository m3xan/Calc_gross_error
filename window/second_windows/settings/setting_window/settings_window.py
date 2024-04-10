"""
Переделать логику
"""
import logging

from PySide6.QtWidgets import QHBoxLayout, QLabel, QComboBox, QSizePolicy
from PySide6.QtCore import Slot

from window.abstract_model.models import AbstractDialog
from window.second_windows.settings.setting_window.settings_window_class import Ui_Dialog


class SettingDialog(AbstractDialog):
    """
    Класс окна настроек интерфейса
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.change_theme()
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
        self.change_theme()

    def __save(self):
        for i in self.comdo_box:
            name = i.currentData()[0]
            data = i.currentData()[1]
            self.settings.save_data_json('window', data, name)
        logging.info('save_window_theme')

    def start(self):
        user_id = self.settings.get_user_id()
        try:
            self.comdo_box: list[QComboBox] = []

            self.settings.set_user_id('option')
            loading = self.settings.load_category_json('window')
            self.settings.set_user_id(user_id)
            user_settings = self.settings.load_category_json('window')
            for name_property in loading:

                label = QLabel(loading[name_property]['name'])
                variation = loading[name_property]['option']
                user_setting = user_settings[name_property]

                combo_box = QComboBox()
                self.comdo_box.append(combo_box)
                for variation_name in variation:
                    combo_box.addItem(
                        variation_name,
                        (name_property, variation[variation_name])
                    )

                combo_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                combo_box.setCurrentText(
                    self.__find_key(variation, user_setting)
                )

                second_layout = QHBoxLayout()
                second_layout.addWidget(label)
                second_layout.addWidget(combo_box)

                self.ui.verticalLayout_3.addLayout(second_layout)
        finally:
            self.settings.set_user_id(user_id)

    def __find_key(self, dict_: dict, search_value):
        for key, value in dict_.items():
            if value == search_value:
                return key
        return None
