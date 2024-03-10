"""
add_window
"""
from datetime import datetime

from PySide6.QtWidgets import QDialog, QInputDialog, QLineEdit, QMessageBox, QListWidgetItem
from PySide6.QtCore import Qt, Signal

from window.second_windows.add_window import add_push_button
from window.second_windows.add_window.add_window_class import Ui_Dialog
from window.data_class_for_window.dataclass import DataclassAddWindow

from settings.settings import load_theme

class AddDialog(QDialog):
    """
    class add_window
    """
    full_data: Signal = Signal(dict)
    def __init__(self, user_id):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.state = DataclassAddWindow(
            change_mode= False,
            save_data_mode= True,
            theme= load_theme(self, user_id)
        )

        # button
        self.ui.push_button_delite_data.clicked.connect(self.push_button_delite_click)
        self.ui.push_button_ok.clicked.connect(self.push_button_ok_click)
        self.ui.push_button_esc.clicked.connect(self.push_button_esc_click)

        # listWidget
        self.ui.list_widget.itemDoubleClicked.connect(self.editValue)
        self.ui.list_widget.itemDoubleClicked.connect(self.change_stat)

        # start
        self.add_item()
        # начинает цикл запроса данных


    def add_item(self):

        item = QListWidgetItem()
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)  # Добавляем возможность редактирования значения
        self.ui.list_widget.addItem(item)

        # Выделяем новый элемент и запускаем его редактирование
        self.editValue(item)

    def change_stat(self):
        self.state.change_mode = True

    def editValue(self, item):
        index = self.ui.list_widget.row(item)
        edit = QLineEdit(self)
        edit.setText(item.text())
        edit.returnPressed.connect(lambda: self.saveValue(item, index, edit))
        self.ui.list_widget.setItemWidget(item, edit)
        edit.setFocus()
        self.state.save_data_mode = False

    def saveValue(self, item, index, edit):
        new_value = edit.text()

        # Проверяем, заполнено ли новое значение
        if new_value == '':
            return
        if self.state.change_mode:
            self.ui.list_widget.takeItem(index)
            item.setText(new_value)
            self.ui.list_widget.insertItem(index, item)
            edit.deleteLater()
            self.state.save_data_mode = False
            self.state.change_mode = False
        else:
            self.ui.list_widget.takeItem(index)
            item.setText(new_value)
            self.ui.list_widget.insertItem(index, item)
            edit.deleteLater()
            self.state.save_data_mode = False
            self.add_item()

    def push_button_remove_click(self):
        currentIndex = self.ui.list_widget.currentRow()
        item = self.ui.list_widget.item(currentIndex)
        if item is not None:
            text, ok = QInputDialog.getText(self,"Изменить запись","Новая запить",QLineEdit.Normal,item.text())
            if text and ok is not None:
                item.setText(text)
        add_push_button.remove_click()

    def push_button_delite_click(self):
        currentIndex = self.ui.list_widget.currentRow()
        item = self.ui.list_widget.item(currentIndex)
        if item.text() == '':
            print('Нельзя удалить пустой элемент')
        else:
            question = QMessageBox.question(self,"Удалить ззначение",
                                            "Вы хотите удалить значение?\n" + item.text(),
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            if question == QMessageBox.StandardButton.Yes:
                item = self.ui.list_widget.takeItem(currentIndex)
            add_push_button.delite_click()

    def push_button_ok_click(self):

        full_data = {}
        c = [[],[]]
        for i in range(0, self.ui.list_widget.count() - 1):
            c[0].append(float(self.ui.list_widget.item(i).text()))
        if self.ui.line_edit_name.text() != '':
            full_data[self.ui.line_edit_name.text()+' '+str(datetime.now())] = c
        else:
            full_data['Измерения '+ str(datetime.now())] = c
        if self.full_data != full_data:
            self.full_data.emit(full_data)
            self.state.save_data_mode = True
        else:
            self.full_data = full_data
        add_push_button.ok_click()

    def push_button_esc_click(self):
        if  self.state.save_data_mode is True:
            self.close()
        elif self.state.save_data_mode is False:
            question = QMessageBox.question(self,"Выход",
                                            "Вы хотите сохранить прогресс перед выходом?",
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                            )

            if question == QMessageBox.StandardButton.Yes:
                self.close()
            elif question == QMessageBox.StandardButton.No:
                print('При выходе нажато нет')

    add_push_button.esc_click()
