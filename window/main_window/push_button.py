from PySide6.QtWidgets import QMessageBox

def push_button_create_graph_click():
    print('push_button_create_graph_click')

def push_button_create_calc_click():
    print('push_button_create_calc_click')

def delite_click(self) -> bool:
    currentIndex = self.ui.list_widget_value.currentRow()
    item = self.ui.list_widget_value.item(currentIndex)
    if item:
        question = QMessageBox.question(self, "Удалить значение",
                                        "Вы хотите удалить значение?\n" + item.text(),
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if question == QMessageBox.StandardButton.Yes:
            self.ui.list_widget_value.takeItem(currentIndex)
            key = self.ui.combo_box_selection_data.currentData()
            self.state.data[key][0].pop(currentIndex)
            return True
