"""
Главное окно
"""
from functools import partial
import logging

import numpy as np
from matplotlib.backends.backend_qt import NavigationToolbar2QT
from PySide6.QtWidgets import QVBoxLayout, QListWidgetItem, QLineEdit
from PySide6.QtCore import Qt, QTimer

from window.abstract_model.models import AbstractWindow
from window.data_class_for_window.dataclass import DataclassMainWindow
from window.main_window.main_window_class import Ui_MainWindow
from window.main_window.custom_context_menu import context_menu
from window.main_window.interior_window.graph_window.graph_window import GraphWindow
from window.main_window import menu_bar, push_button
from window.second_windows.add_window.add_window import AddDialog
from window.second_windows.settings.main_settings.setting_window import SettingsDialog
from window.second_windows.load_window.load_window import LoadDialog

from data_base.test_orm import DatabaseUsersHandler
from functions.calcul.calc import Calculator, Romanovski

from functions.graph.graph import GraphicMaker
from functions.excel.excel import get_name_column
from functions.settings.settings import JsonSettings

from functions.decorator.timer import timer_decorator
from functions.decorator.printing import print_return

from functions.loger import Logger

@timer_decorator
#TODO переделать заполнение лист виджета
class MainWindow(AbstractWindow):
    """
    class MainWindow
    """
    def __init__(self, user_id: int):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.bd = DatabaseUsersHandler(user_id)
        self.settings = JsonSettings()

        self.state = DataclassMainWindow(
            active_mod= None, # данное условие писать с использование math case
            save_data_mode= True,
            data= {},
            excel_path= None,
            change_mode= False,
            add_mod= False,
            user_id= user_id,
            clearance_level = self.bd.select_user().clearance_level,
            auto_save_time= self.settings.load_category_json('auto_save'),
            theme= self.change_theme(user_id),
        )

        self.__init_graph()
        if self.state.auto_save_time['switched']:
            self.__init_timer()

        if self.state.clearance_level > 1:
            Logger().change_logger(user_id, logging.INFO)
            self.__add_notion()
        else:
            Logger().change_logger(user_id)

        self.__init_reaction()

    # menubar
    @print_return
    def action_bd_click(self):
        """
        on action bd clicked
        """
        self.windows = LoadDialog()
        self.windows.show()
        self.state.data = self.bd.test_select_2(user_id= self.state.user_id)
        self.windows.close()
        menu_bar.action_bd_click()
        self.enable_ui(True)
        if any(self.state.data):
            self.ui.combo_box_selection_data.clear()
            for key in self.state.data:
                self.ui.combo_box_selection_data.addItem(
                    key[1],
                    key
                )
        # change
        self.state.active_mod = 'bd'
        return f'self.state.active_mod = {self.state.active_mod}, {self.state.data}'

    @print_return
    def action_excel_click(self):
        """
        on excel bd clicked
        """
        if menu_bar.action_excel_click(self):
            # change
            self.state.active_mod = 'excel'
            self.timer.start(self.state.auto_save_time['time'])
            self.enable_ui(True)
            return self.state.active_mod, self.state.excel_path, self.state.data, self.timer.isActive()
        return None

    @print_return
    def action_save_click(self):
        """
        on save clicked
        """
        if not self.state.save_data_mode:

            match self.state.active_mod:

                case 'excel':
                    menu_bar.action_save_excel_click(self)
                    # change
                    self.state.save_data_mode = True
                    return self.state.save_data_mode

                case 'bd':
                    menu_bar.action_save_bd_click()
                    # change
                    self.state.save_data_mode = True
                    return self.state.save_data_mode

        return None

    @print_return
    def action_esc_click(self):
        """
        on esc clicked
        переписать не используя QMessageBox
        """
        return menu_bar.action_esc_click(self)

    def action_info_click(self):
        """
        Открывает окно "О нас"
        """
        return menu_bar.action_info_click(self)

    @staticmethod
    def action_help_click(): # ДОДЕЛАНО
        """
        Открывает пользовательскую документацию
        """
        return menu_bar.action_help_click()

    def action_new_click(self):
        """
        МБ переписать
        """
        dialog = AddDialog(self.state.user_id)
        dialog.full_data.connect(self.add_selection_data)
        return dialog.exec()
        # change
        # передаёт full_data

    def action_save_as_click(self):
        """
        on save_as clicked
        """
        if self.state.data:
            return menu_bar.save_as_click(self)
        return None


    def action_setting_window_click(self):
        """
        open satting_widow
        """
        setting_widow = SettingsDialog(self.state.user_id)
        setting_widow.windowThemeChanged.connect(self.__update_ui)
        return setting_widow.exec()

    # button
    def push_button_create_graph_click(self):
        """
        Create graph
        """
        push_button.push_button_create_graph_click()
        self.plt_tool_bar.update()
        self.sc.ax.clear()
        hist = self.state.data[self.ui.combo_box_selection_data.currentData()][0]
        n, bins, _ = self.sc.ax.hist(hist, rwidth=0.8, color='#ff8921', label= 'Распределение')

        bin_centers = 0.5 * (bins[:-1] + bins[1:])

        window_size = 5  # Размер окна для усреднения, можно добавить изменение в настройки измерения
        weights = np.ones(window_size) / window_size  # Веса для усреднения значений

        smoothed_hist = np.convolve(n, weights, mode='same')  # Применение усреднения по скользящему окну

        aligned_bin_centers = bin_centers[:len(smoothed_hist)]
        self.sc.ax.plot(aligned_bin_centers, smoothed_hist, '-o', label='Прямая')

        self.sc.update_collor(
            self.state.theme[1]['canvas'],
            self.state.theme[1]['text']
        )
        self.sc.ax.legend()
        self.sc.draw()

    def push_button_create_calc_click(self):
        """
        create_calc
        """
        self.ui.list_widget_answer.clear()
        calculator = Calculator(Romanovski())
        answers = calculator.calculate_with(
            self.state.data[self.ui.combo_box_selection_data.currentData()][0]
        )
        for answer in answers:
            self.ui.list_widget_answer.addItem(str(answer))
        self.state.save_data_mode = False
        return f'self.state.save_data_mode = {self.state.save_data_mode}'

    def push_button_add_data_click(self):# ПЕРЕДЕЛАТЬ
        """
        add data
        """
        self.add_item()
        self.state.save_data_mode = False

        return f'self.state.save_data_mode = {self.state.save_data_mode}'

    def push_button_delite_data_click(self):# ПЕРЕДЕЛАТЬ
        """
        delite carent element
        """
        if self.state.active_mod:
            if push_button.delite_click(self):
                self.state.save_data_mode = False
                return f'self.state.save_data_mode = {self.state.save_data_mode}'
        return None

    # combobox
    def combo_box_selection_data_changed(self):
        """
        заглушка
        """
        self.fill_listWidget()

    # contextmenu
    def custom_context_menu_open(self, pos):
        """
        заглушка
        """
        # сделать что бы работало только с лист виджетом
        if self.state.active_mod:
            context_menu.menu(self, pos)

    # __init__
    def __init_graph(self):
        """
        заглушка
        """
        graphic_maker = GraphicMaker()
        self.sc = graphic_maker.empty_with_axes(
            color_text= self.state.theme[1]['text'],
            color_fig= self.state.theme[1]['canvas']
        )

        self.graphwindow = GraphWindow()
        self.plt_tool_bar = NavigationToolbar2QT(self.sc)
        self.graphwindow.graph.toolBar.insertWidget(self.graphwindow.graph.action_create_graph, self.plt_tool_bar)
        self.graphwindow.setCentralWidget(self.sc)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.insertWidget(0, self.graphwindow)

        self.ui.frame.setLayout(layout)

    def __init_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.action_save_click)

    def __init_main_list_widget_value(self):
        self.ui.list_widget_value.itemDoubleClicked.connect(self.editValue)
        self.ui.list_widget_value.itemDoubleClicked.connect(self.change_stat)
        self.ui.list_widget_value.customContextMenuRequested.connect(self.custom_context_menu_open)

    def __init_main_combobox(self):
        self.ui.combo_box_selection_data.currentIndexChanged.connect(self.combo_box_selection_data_changed)

    def __init_main_button(self):
        self.ui.push_button_create_calc.clicked.connect(self.push_button_create_calc_click)
        self.ui.push_button_add_data.clicked.connect(self.add_item)
        self.ui.push_button_delite_data.clicked.connect(self.push_button_delite_data_click)

    def __init_main_action(self):
        self.ui.action_new.triggered.connect(self.action_new_click)
        self.ui.action_excel.triggered.connect(self.action_excel_click)
        self.ui.action_bd.triggered.connect(self.action_bd_click)
        self.ui.action_save.triggered.connect(self.action_save_click)
        self.ui.action_save_as.triggered.connect(self.action_save_as_click)
        self.ui.action_esc.triggered.connect(self.action_esc_click)

        self.ui.action_setting_window.triggered.connect(self.action_setting_window_click)
        self.ui.action_calc.triggered.connect(self.action_setting_window_click)

        self.ui.action_help.triggered.connect(self.action_help_click)

        self.ui.action_info.triggered.connect(self.action_info_click)

    def __init_graph_menubar(self):
        self.graphwindow.graph.action_create_graph.triggered.connect(self.push_button_create_graph_click)

    def __init_reaction(self):
        self.__init_graph_menubar()
        self.__init_main_action()
        self.__init_main_button()
        self.__init_main_combobox()
        self.__init_main_list_widget_value()

    @print_return
    def __add_notion(self):
        return 'сделать что-то'

    # helpfull
    def __update_ui(self, signal):

        self.state.theme = self.change_theme(signal)

        self.graphwindow.addToolBar(
            eval(
                self.settings.load_attribute('window', 'toolBar')
            ),
            self.graphwindow.graph.toolBar
        )

        self.addDockWidget(
            eval(
                self.settings.load_attribute('window','dockWidget')
            ),
            self.ui.dockWidget
        )

        self.sc.update_collor(
            self.state.theme[1]['canvas'],
            self.state.theme[1]['text']
        )

        self.sc.draw()

    def __enabled_action(self, enable: bool):
        self.ui.action_save.setEnabled(enable)
        self.ui.action_save_as.setEnabled(enable)

    def __enabled_dock_widget(self, enable: bool):
        self.ui.dockWidget.setEnabled(enable)

        self.ui.combo_box_selection_data.setEnabled(enable)
        self.ui.list_widget_value.setEnabled(enable)
        self.ui.list_widget_answer.setEnabled(enable)

        self.ui.push_button_add_data.setEnabled(enable)
        self.ui.push_button_delite_data.setEnabled(enable)
        self.ui.push_button_create_calc.setEnabled(enable)

    def enable_ui(self, enable: bool):
        """
        eneble actioan and dock_widget
        """
        self.__enabled_action(enable)
        self.__enabled_dock_widget(enable)
        self.graphwindow.graph.action_create_graph.setEnabled(enable)

    def add_item(self):
        """
        add item on combo_box_selection_data
        """
        if self.ui.combo_box_selection_data.currentIndex() != -1 and not self.state.add_mod:
            self.state.add_mod = True
            item = QListWidgetItem()
            item.setFlags(item.flags() | Qt.ItemIsEditable)  # Добавляем возможность редактирования значения
            self.ui.list_widget_value.addItem(item)

            # Выделяем новый элемент и запускаем его редактирование
            self.editValue(item)

    def closeEvent(self, event):
        """
        заглушка
        """
        self.save_settings()
        logging.info('main window close')
        event.accept()  # Подтверждаем закрытие окна

    def save_settings(self):
        """
        заглушка
        """

        tool_bar_area = f'Qt.{str(self.graphwindow.toolBarArea(self.graphwindow.graph.toolBar))[12:]}'
        dock_widget_area = f'Qt.{str(self.dockWidgetArea(self.ui.dockWidget))[15:]}'
        try:
            self.settings.save_data_json('window', tool_bar_area, 'toolBar')
            self.settings.save_data_json('window', dock_widget_area, 'dockWidget')
            logging.info('save settings')
            return True
        except FileNotFoundError as err:
            logging.error(err, exc_info= True)

    def fill_listWidget(self): # ПЕРЕСМОРЕТЬ ЧТО МОЖНО УПРОСТИТЬ
        """
        При разных типах ввода разные условия и разные другие параметры
        заготовка на будещее
        """
        self.ui.list_widget_value.clear()
        match self.state.active_mod:
            case 'bd':
                if self.state.data is not None and self.ui.combo_box_selection_data.currentData() is not None:
                    return self.add_elem_on_list_winget()

            case 'excel':
                return self.add_elem_on_list_winget()

            case _:
                return self.add_elem_on_list_winget()

    def add_elem_on_list_winget(self):
        """
        заглушка
        """
        key = self.ui.combo_box_selection_data.currentData()
        try:
            for numder in self.state.data[key][0]:
                self.ui.list_widget_value.addItem(str(numder))
            return True
        except KeyError as err:
            logging.error(err, exc_info= True)

    def add_selection_data(self, full_data): # ПЕРЕСМОТЕРТЬ
        """
        заглушка
        """

        # ПЕРЕПИСАТЬ ВСЮ ФУНКЦИ
        if self.state.data:
            index = self.ui.combo_box_selection_data.count()
            last_index = self.ui.combo_box_selection_data.itemData(index-1)[0]
            c = get_name_column(1, full_data)
            m = last_index+1, c , False, ()
            self.state.data[m] = full_data.get(c)
            if index:
                self.ui.combo_box_selection_data.addItem(
                    c,
                    m
                )
                self.fill_listWidget()
            else:
                self.ui.combo_box_selection_data.addItem(
                    c,
                    m
                )
                self.fill_listWidget()

        else:
            # переделать
            c = get_name_column(1, full_data)
            m = 1, c , False, ()
            self.state.data[m] = full_data.get(c)
            self.ui.combo_box_selection_data.addItem(
                c,
                m
            )
            # self.fill_listWidget()
        self.enable_ui(True)
        self.state.save_data_mode = False

    def on_change(self, read_excel_signal):
        """
        заглушка
        """
        menu_bar.on_change(self, read_excel_signal)

    def editValue(self, item):
        """
        заглушка
        """
        index = self.ui.list_widget_value.row(item)
        edit = QLineEdit(self)
        edit.setText(item.text())
        edit.returnPressed.connect(partial(self.saveValue, item, index, edit))
        self.ui.list_widget_value.setItemWidget(item, edit)
        edit.setFocus()
        self.state.save_data_mode = False

    def saveValue(self, item, index, edit):
        """
        заглушка
        """
        new_value = edit.text()

        # Проверяем, заполнено ли новое значение
        if new_value == '':
            return
        if self.state.change_mode:
            b = self.ui.combo_box_selection_data.currentData()
            self.state.data[b][0][index] = float(new_value)

            edit.deleteLater()
            self.ui.list_widget_value.takeItem(index)
            item.setText(str(float(new_value)))
            self.ui.list_widget_value.insertItem(index, item)

            self.state.save_data_mode = False
            self.state.change_mode = False
        else:
            self.ui.list_widget_value.takeItem(index)
            item.setText(str(float(new_value)))
            self.ui.list_widget_value.insertItem(index, item)
            b = self.ui.combo_box_selection_data.currentData()
            self.state.data[b][0].append(float(new_value))
            edit.deleteLater()
            self.state.add_mod = False
            self.state.save_data_mode = False

    def change_stat(self):
        """
        заглушка
        """
        self.state.change_mode = True
