"""
Переделать логику
"""

from PySide6.QtWidgets import QHBoxLayout, QLabel, QComboBox, QSizePolicy
from PySide6.QtCore import Signal

from window.second_windows.settings.setting_window.settings_window_class import Ui_Dialog, QDialog
from window.data_class_for_window.dataclass import BaseDataclassWindows

from settings.settings import save_data_json, load_theme, load_category_json, load_attribute

def find_key(dict_: dict, search_value):
    for key, value in dict_.items():
        if value == search_value:
            return key

class SettingDialog(QDialog):
    change_theme = Signal(bool)
    """
    Класс окна настроек интерфейса
    """
    def __init__(self, user_id):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.state = BaseDataclassWindows(
            theme= load_theme(self, user_id)
        )
        self.user_id = user_id

        self.start()

        # push_button
        self.ui.push_button_save.clicked.connect(self.push_button_save_clicked)
        self.ui.push_button_esc.clicked.connect(self.push_button_esc_clicked)
        self.ui.push_button_restart.clicked.connect(self.push_button_restart_clicked)

    def push_button_save_clicked(self):
        for i in self.comdo_box:

            name = i.currentData()[0]
            data = i.currentData()[1]

            save_data_json('window', name, data, self.user_id)
        print('save_presed')

    def push_button_esc_clicked(self):
        self.close()

    def push_button_restart_clicked(self):
        self.push_button_save_clicked()
        self.state.theme= load_theme(self, self.user_id)
        self.change_theme.emit(True)

    def start(self):
        self.comdo_box = []
        loading = load_category_json('window', 'option')
        for name_property in loading:
            label = QLabel(loading[name_property]['name'])
            variation = load_attribute('window', name_property, 'option')['option']
            user_setting = load_attribute('window',name_property, self.user_id)
            # тутдоделать что бы ставилось что у пользователя
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
                find_key(variation, user_setting)
            )

            second_layout = QHBoxLayout()
            second_layout.addWidget(label)
            second_layout.addWidget(combo_box)

            self.ui.verticalLayout_3.addLayout(second_layout)
