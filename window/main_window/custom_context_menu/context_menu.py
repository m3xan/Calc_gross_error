from PySide6.QtWidgets import QMenu

def menu(self, pos):
    selected_item = self.ui.list_widget_value.indexAt(pos)
    context_menu = QMenu(self)

    if selected_item.row() != -1:
        # Клик произошел на элементе списка
        add_action = context_menu.addAction('Добавить')
        change_action = context_menu.addAction('Изменить')
        del_action = context_menu.addAction('Удалить')

        action = context_menu.exec(self.ui.list_widget_value.mapToGlobal(pos))

        if action == add_action:
            self.add_item()

        elif action == change_action:
            self.change_stat()
            self.editValue(self.ui.list_widget_value.currentItem())

        elif action == del_action:
            self.push_button_delite_data_click()

    else:
        # Клик произошел вне элементов списка
        some_action = context_menu.addAction('Добавить')

        action = context_menu.exec(self.ui.list_widget_value.mapToGlobal(pos))

        if action == some_action:
            self.add_item()
