"""
add_window
"""
from datetime import datetime

from PySide6.QtWidgets import QInputDialog, QLineEdit, QMessageBox, QListWidgetItem
from PySide6.QtCore import Qt, Signal

from window.abstract_model.models import AbstractDialog
from window.second_windows.add_window.add_window_class import Ui_Dialog
from window.data_class_for_window.dataclass import DataclassAddWindow

from data_class.data import Data

class AddDialog(AbstractDialog):
    """
    class add_window
    """
    full_data: Signal = Signal(Data)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.state = DataclassAddWindow(
            change_mode= False,
            save_data_mode= True,
        )
        self.change_theme()

        self.ui.push_button_delite_data.clicked.connect(self.push_button_delite_click)
        self.ui.push_button_ok.clicked.connect(self.push_button_ok_click)
        self.ui.push_button_esc.clicked.connect(self.push_button_esc_click)

        self.ui.list_widget.itemDoubleClicked.connect(self.change_stat)
        self.ui.list_widget.itemDoubleClicked.connect(self.editValue)

        # start
        self.add_item()

    def add_item(self):
        item = QListWidgetItem()
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)  # Добавляем возможность редактирования значения
        self.ui.list_widget.addItem(item)

        # Выделяем новый элемент и запускаем его редактирование
        self.editValue(item)

    def change_stat(self):
        self.state.change_mode = True

    def editValue(self, item):
        if not self.state.change_mode:
            index = self.ui.list_widget.row(item)
            edit = QLineEdit(self)
            edit.setText(item.text())
            edit.returnPressed.connect(lambda: self.saveValue(item, index, edit))
            self.ui.list_widget.setItemWidget(item, edit)
            edit.setFocus()
            self.state.save_data_mode = False

    def saveValue(self, item: QListWidgetItem, index, edit: QLineEdit):
        new_value = edit.text()

        if not self.__walid_value(new_value):
            return
        self.ui.list_widget.takeItem(index)
        item.setText(f'{float(new_value)}')
        self.ui.list_widget.insertItem(index, item)
        edit.deleteLater()
        if self.state.change_mode:
            self.state.save_data_mode = False
            self.state.change_mode = False
        else:
            self.state.save_data_mode = False
        self.add_item()

    def push_button_remove_click(self):
        currentIndex = self.ui.list_widget.currentRow()
        item = self.ui.list_widget.item(currentIndex)
        if item is not None:
            text, ok = QInputDialog.getText(
                self,
                'Изменить запись',
                'Новая запить',
                QLineEdit.Normal,
                item.text()
            )
            if text and ok is not None:
                item.setText(text)

    def push_button_delite_click(self):
        current_index = self.ui.list_widget.currentRow()
        item = self.ui.list_widget.item(current_index)
        if item.text() == '':
            print('Нельзя удалить пустой элемент')
        else:
            question = QMessageBox.question(
                self,
                'Удалить ззначение',
                f'Вы хотите удалить значение?\n{item.text()}',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if question == QMessageBox.StandardButton.Yes:
                item = self.ui.list_widget.takeItem(current_index)

    def push_button_ok_click(self):
        data = Data(metadate= True)
        if self.ui.line_edit_name.text() != '' and len(self.ui.line_edit_name.text()) <= 50:
            name_calc = f'{self.ui.line_edit_name.text()} {datetime.now()}'
        else:
            name_calc = f'Измерения {datetime.now()}'

        data.append_name(name_calc)

        for i in range(0, self.ui.list_widget.count() - 1):
            data.append_value(
                (0, name_calc),
                float(self.ui.list_widget.item(i).text())
            )

        self.full_data.emit(data)
        self.close()

    def push_button_esc_click(self):
        if self.state.save_data_mode is True:
            self.close()
        else:
            question = QMessageBox.question(
                self,
                'Выход',
                'Вы хотите сохранить прогресс перед выходом?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            if question == QMessageBox.StandardButton.Yes:
                self.push_button_ok_click()
            else:
                pass

    def __walid_value(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
