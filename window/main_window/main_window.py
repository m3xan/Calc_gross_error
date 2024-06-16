"""
Главное окно
"""
from datetime import datetime
import os
from functools import partial
import logging

import numpy as np
from matplotlib.backends.backend_qt import NavigationToolbar2QT
from PySide6.QtWidgets import QVBoxLayout, QListWidgetItem, QLineEdit, QFileDialog, QMessageBox, QMenu
from PySide6.QtCore import Qt, QTimer, Slot

from window.abstract_model.models import AbstractWindow
from window.data_class_for_window.dataclass import DataclassMainWindow
from window.main_window.main_window_class import Ui_MainWindow
from window.main_window.interior_window.graph_window.graph_window import GraphWindow
from window.second_windows import (
    AddDialog,
    SettingsDialog,
    MethodsDialog,
    LoadDialog,
    AboutDialog,
)

from functions import logger
from functions.settings.pydantic_model import MainWindowElement
from functions.calculate import Calculator, method_map
from functions.graph import GraphicMaker

from thread import ReadThread, SaveAsThread, SaveThread

from data_class.data import Data

from global_param import FilePath

class MainWindow(AbstractWindow):
    """
    class MainWindow
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.state = DataclassMainWindow(
            active_mod= None, # use math case
            save_data_mode= True,
            data= None,
            excel_path= None,
            change_mode= False,
            add_mod= False,
            clearance_level= self.user_db.select_user().clearance_level,
            auto_save_time= self.settings.load_json().auto_save,
        )
        self.change_theme()

        self.__init_graph()
        if self.state.auto_save_time.switched:
            self.__init_timer()
        logger_ = logger.Logger()
        if self.state.clearance_level > 1:
            logger_.change_logger(self.user_db.get_id(), logging.INFO)
        else:
            logger_.change_logger(self.user_db.get_id())

        self.__init_reaction()

    # menubar
    @Slot()
    @logger.info
    def __action_bd_click(self):
        self.read_thread = ReadThread()
        self.read_thread.read_signal.connect(self.on_change)
        self.read_thread.start()
        self.load_window = LoadDialog()
        self.load_window.exec()

        self.state.active_mod = 'bd'
        return f'{self.state.active_mod=}, {dict(self.state.data)=}'

    @Slot()
    @logger.info
    def __action_excel_click(self):
        self.state.excel_path = QFileDialog().getOpenFileName(
            caption='Выбрать файл',
            dir=os.path.join(os.getenv('userprofile')),
            filter= 'Excel File (*.xlsx;*.xlsm;*.xltx;*.xltm)'
        )
        if self.state.excel_path != ('', ''):
            self.read_thread = ReadThread(self.state.excel_path[0])
            self.read_thread.start()
            self.read_thread.read_signal.connect(self.on_change)
            self.load_window = LoadDialog()
            self.load_window.exec()
            if self.state.auto_save_time.switched:
                self.timer.start(self.state.auto_save_time.time)
                logging.info('timer on')

            self.state.active_mod = 'excel'
            return f'{self.state.active_mod=}, {self.state.excel_path=}, {dict(self.state.data)=}'
        return None

    @Slot()
    @logger.info
    def action_save_click(self):
        """
        on save data
        """
        match self.state.active_mod:
            case 'excel':
                self.save_tread = SaveThread(self.state.data, self.state.excel_path[0])
                self.save_tread.saved.connect(self.__set_data)
                self.save_tread.start()
                return f'{self.state.save_data_mode=}'
            case 'bd':
                self.save_tread = SaveThread(self.state.data)
                self.save_tread.saved.connect(self.__set_data)
                self.save_tread.start()
                return f'{self.state.save_data_mode=}'
            case _:
                logging.critical(f'not valid file {self.state.active_mod=}')
                return None

    @Slot(Data)
    def __set_data(self, data: Data):
        self.save_tread.deleteLater()
        self.state.data = data
        self.state.save_data_mode = True
        return f'{self.state.save_data_mode=}'

    @Slot()
    def action_esc_click(self):
        """
        on esc clicked
        """
        if self.state.save_data_mode is True:
            self.close()
        else:
            result = QMessageBox.question(
                self,
                "Сохранить?",
                "Cохранить результат?",
                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No,
                defaultButton = QMessageBox.StandardButton.Ok
            )
            if result == QMessageBox.StandardButton.Ok:
                self.action_save_click()
                self.close()

    @Slot()
    @logger.info
    def action_info_click(self):
        """
        Открывает окно "О нас"
        """
        dialog = AboutDialog()
        return dialog.exec()

    @Slot()
    @logger.debug
    @staticmethod
    def action_help_click():
        """
        Открывает пользовательскую документацию
        """
        try:
            os.startfile(FilePath().documentation)
            return True
        except FileNotFoundError as err:
            raise err

    @Slot()
    @logger.debug
    def action_new_click(self):
        """
        МБ переписать
        """
        dialog = AddDialog()
        dialog.full_data.connect(self.add_selection_data)
        return dialog.exec()

    @Slot()
    @logger.debug
    def action_save_as_click(self):
        """
        on save_as clicked
        """
        if self.state.data:
            file_name = QFileDialog.getSaveFileName(
            self,
            'Сохранить как:',
            f'{os.path.join(os.getenv("userprofile"), f'Измерения {datetime.now().strftime('%d-%m-%Y %H.%M.%S')}')}',
            filter= 'Книга Excel (*.xlsx)')
            if file_name != ('', ''):
                self.save_as_thread = SaveAsThread(file_name[0], self.state.data)
                self.save_as_thread.start()
                return True
        return None

    @Slot()
    @logger.debug
    def action_setting_window_click(self):
        """
        open satting_widow
        """
        setting_widow = SettingsDialog()
        setting_widow.windowThemeChanged.connect(self.__update_ui)
        return setting_widow.exec()

    @Slot()
    @logger.debug
    def __action_delite_click(self):
        item  = self.ui.combo_box_selection_data.currentData()
        if item:
            question = QMessageBox.question(
                self,
                'Удалить значение',
                f'Вы хотите удалить значение?\n{item[1]}',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if question == QMessageBox.StandardButton.Yes:
                del self.state.data[item]

                self.ui.combo_box_selection_data.removeItem(
                    self.ui.combo_box_selection_data.currentIndex()
                )
                self.state.save_data_mode = False
        return f'{self.state.save_data_mode=}'

    @Slot()
    @logger.debug
    def __action_calc_click(self):
        dialog = MethodsDialog()
        return dialog.exec()


    @Slot()
    @logger.info
    def _push_button_create_graph_click(self):
        if not self.state.data:
            return False
        self.plt_tool_bar.update()
        self.canvbar.ax.clear()
        settings = self.settings.load_json()
        hist = [
            data[1] for data in self.state.data[self.ui.combo_box_selection_data.currentData()][0]
        ]
        n, bins, _ = self.canvbar.ax.hist(hist, rwidth= 0.8, color= '#ff8921', label= 'Распределение')
        bin_centers = 0.5 * (bins[:-1] + bins[1:])

        weights = np.ones(settings.graph_settinsgs.window_size) / settings.graph_settinsgs.window_size
        smoothed_hist = np.convolve(n, weights, mode='same')

        aligned_bin_centers = bin_centers[:len(smoothed_hist)]
        self.canvbar.ax.plot(aligned_bin_centers, smoothed_hist, '-o', label= 'Кривая распределения')

        self.canvbar.update_collor(
            settings.window.canvas_settings.canvas,
            settings.window.canvas_settings.text
        )
        self.canvbar.ax.legend()
        self.canvbar.draw()
        return True

    @Slot()
    @logger.debug
    def _push_button_create_calc_click(self):
        """
        create_calc
        """
        user_settings = self.settings.load_calculation()
        method_ = user_settings.method
        significance_level = user_settings.significance_level
        name_calc = self.ui.combo_box_selection_data.currentData()

        calculator = Calculator()
        calculator.method = method_map[method_]()

        answers = calculator.calculate_with(
            [data[1] for data in self.state.data.value(name_calc)],
            significance_level
        )
        self.__set_answer(answers)

        self.state.save_data_mode = False
        return f'{method_=}, {significance_level=}, {self.state.save_data_mode=}'

    @Slot()
    @logger.debug
    def push_button_add_data_click(self):
        """
        add data
        """
        self.add_item()
        self.state.save_data_mode = False
        return f'{self.state.save_data_mode=}'

    @Slot()
    @logger.debug
    def push_button_delite_data_click(self):
        """
        delite carent element
        """
        if self.state.active_mod:
            current_index = self.ui.list_widget_value.currentRow()
            if item := self.ui.list_widget_value.item(current_index):
                question = QMessageBox.question(
                    self,
                    'Удалить значение',
                    f'Вы хотите удалить значение?\n{item.text()}',
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
                if question == QMessageBox.StandardButton.Yes:
                    self.ui.list_widget_value.takeItem(current_index)
                    self.state.data.delite_value(
                        self.ui.combo_box_selection_data.currentData(),
                        current_index)
                    self.state.save_data_mode = False
                return f'{self.state.save_data_mode=}'
        return None

    @Slot(Data)
    def on_change(self, read_signal: Data):
        """
        заглушка
        """
        self.load_window.close()
        self.read_thread.quit()
        if read_signal:
            self.state.data = read_signal
            self.ui.combo_box_selection_data.clear()
            for key in self.state.data.name():
                self.ui.combo_box_selection_data.addItem(
                    key[1], key)
        self.state.data.set_metadate(True)
        self.fill_listwidget()
        self.enable_ui(True)

    @logger.debug
    def __init_graph(self):
        """
        primary initialization of the chart window
        and inserting it into the frame
        """
        settings = self.settings.load_canvas()
        graphic_maker = GraphicMaker()
        self.canvbar = graphic_maker.empty_with_axes(
            color_text= settings.text,
            color_fig= settings.canvas
        )

        self.graphwindow = GraphWindow()
        self.plt_tool_bar = NavigationToolbar2QT(self.canvbar)
        self.graphwindow.graph.toolBar.insertWidget(
            self.graphwindow.graph.action_create_graph,
            self.plt_tool_bar
        )
        self.graphwindow.setCentralWidget(self.canvbar)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.insertWidget(0, self.graphwindow)

        self.ui.frame.setLayout(layout)
        return True

    def __init_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.action_save_click)

    def __init_main_list_widget_value(self):
        self.ui.list_widget_value.itemDoubleClicked.connect(self.edit_value)
        self.ui.list_widget_value.itemDoubleClicked.connect(self.__change_stat)
        self.ui.list_widget_value.customContextMenuRequested.connect(self.__start_menu)

    def __init_main_combobox(self):
        self.ui.combo_box_selection_data.currentIndexChanged.connect(self.__set_values_answers)

    def __init_main_button(self):
        self.ui.push_button_create_calc.clicked.connect(self._push_button_create_calc_click)
        self.ui.push_button_add_data.clicked.connect(self.push_button_add_data_click)
        self.ui.push_button_delite_data.clicked.connect(self.push_button_delite_data_click)

    def __init_main_action(self):
        self.ui.action_new.triggered.connect(self.action_new_click)
        self.ui.action_excel.triggered.connect(self.__action_excel_click)
        self.ui.action_bd.triggered.connect(self.__action_bd_click)
        self.ui.action_save.triggered.connect(self.action_save_click)
        self.ui.action_save_as.triggered.connect(self.action_save_as_click)
        self.ui.action_esc.triggered.connect(self.action_esc_click)
        self.ui.action_setting_window.triggered.connect(self.action_setting_window_click)
        self.ui.action_calc.triggered.connect(self.__action_calc_click)
        self.ui.action_help.triggered.connect(self.action_help_click)
        self.ui.action_info.triggered.connect(self.action_info_click)
        self.ui.action_delite.triggered.connect(self.__action_delite_click)

    def __init_graph_menubar(self):
        self.graphwindow.graph.action_create_graph.triggered.connect(self._push_button_create_graph_click)

    def __init_elemeth(self):
        self.ui.dockWidget.dockLocationChanged.connect(self.__save_settings)
        self.graphwindow.graph.toolBar.topLevelChanged.connect(self.__save_settings)

    def __init_reaction(self):
        self.__init_graph_menubar()
        self.__init_main_action()
        self.__init_main_button()
        self.__init_main_combobox()
        self.__init_main_list_widget_value()
        self.__init_elemeth()

    def __update_ui(self):
        self.change_theme()
        self._push_button_create_graph_click()
        setting_canvas_ = self.settings.load_canvas()
        setting_window = self.settings.load_window()

        self.graphwindow.addToolBar(
            setting_window.element.toolBar,
            self.graphwindow.graph.toolBar
        )
        self.addDockWidget(
            setting_window.element.dockWidget,
            self.ui.dockWidget
        )
        self.canvbar.update_collor(
            setting_canvas_.canvas,
            setting_canvas_.text
        )
        self.canvbar.draw()

    def __enabled_action(self, enable: bool):
        self.ui.action_save.setEnabled(enable)
        self.ui.action_save_as.setEnabled(enable)
        self.ui.action_new.setEnabled(enable)
        self.ui.action_delite.setEnabled(enable)

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
            item.setFlags(item.flags() | Qt.ItemIsEditable) # Добавляем возможность редактирования значения
            self.ui.list_widget_value.addItem(item)
            # Выделяем новый элемент и запускаем его редактирование
            self.edit_value(item)

    def closeEvent(self, event):
        """
        заглушка
        """
        if self.__save_settings(True):
            logging.info('main window close')
        event.accept()  # Подтверждаем закрытие окна

    @logger.info
    def __save_settings(self, save_start: bool = False) -> bool:
        """
        заглушка
        """

        try:
            settings_ = self.settings.load_json()
            if any((
                self.dockWidgetArea(
                    self.ui.dockWidget
                ) != settings_.window.element.dockWidget,
                self.graphwindow.toolBarArea(
                    self.graphwindow.graph.toolBar
                ) != settings_.window.element.toolBar,
            )):
                settings_.window.element = MainWindowElement(
                    dockWidget= self.dockWidgetArea(self.ui.dockWidget),
                    toolBar= self.graphwindow.toolBarArea(self.graphwindow.graph.toolBar)
                )
            if settings_.save_user_name:
                save = self.user_db.select_user().username
            else:
                save = None
            if save_start:
                self.settings.save_start(save)
            self.settings.save_json(settings_)
            logging.info('save settings')
            return True
        except FileNotFoundError as err:
            logging.error(err, exc_info= True)
            return False

    @logger.info
    def fill_listwidget(self):
        """
        При разных типах ввода разные условия и разные другие параметры
        заготовка на будещее
        """
        self.ui.list_widget_value.clear()
        if self.ui.combo_box_selection_data.currentData():
            try:
                for numder in self.state.data.value(self.ui.combo_box_selection_data.currentData()):
                    self.ui.list_widget_value.addItem(str(numder[1]))
                return True
            except KeyError as err:
                logging.error(err, exc_info= True)
        return False

    def __set_values_answers(self):
        self.fill_listwidget()
        self.__set_method()

    @logger.debug
    def add_selection_data(self, full_data: Data):
        """
        заглушка
        """
        # ПЕРЕПИСАТЬ ВЕСЬ МЕТОД
        self.state.data = full_data
        self.__fill_combo_box_selection_data()
        self.enable_ui(True)
        self.state.save_data_mode = False
        return f'{self.state.save_data_mode=}'

    @logger.debug
    def edit_value(self, item):
        """
        заглушка
        """
        index = self.ui.list_widget_value.row(item)
        edit = QLineEdit(self)
        edit.setText(item.text())
        edit.returnPressed.connect(partial(self.save_value, item, index, edit))
        self.ui.list_widget_value.setItemWidget(item, edit)
        edit.setFocus()
        self.state.save_data_mode = False
        return f'{self.state.save_data_mode=}'

    @logger.debug
    def save_value(self, item, index, edit: QLineEdit):
        """
        заглушка
        """
        new_value = edit.text()
        try:
            if new_value == '':
                return
            new_value = float(new_value)
        except ValueError:
            return

        self.ui.list_widget_value.takeItem(index)
        item.setText(str(new_value))
        self.ui.list_widget_value.insertItem(index, item)
        if self.state.change_mode:
            self.state.data.change_value(
                self.ui.combo_box_selection_data.currentData(),
                index,
                new_value)
        else:
            self.state.data.append_value(
                self.ui.combo_box_selection_data.currentData(),
                new_value)
        edit.deleteLater()

        self.state.add_mod = False
        self.state.save_data_mode = False
        return f'{self.state.add_mod=}, {self.state.save_data_mode=}'

    def __change_stat(self):
        self.state.change_mode = True

    def __start_menu(self, pos):
        if self.state.active_mod:
            selected_item = self.ui.list_widget_value.indexAt(pos)
            context_menu = QMenu(self)
            if selected_item.row() != -1:
                add_action = context_menu.addAction('Добавить')
                change_action = context_menu.addAction('Изменить')
                del_action = context_menu.addAction('Удалить')
                action = context_menu.exec(self.ui.list_widget_value.mapToGlobal(pos))
                if action == add_action:
                    self.push_button_add_data_click()
                elif action == change_action:
                    self.__change_stat()
                    self.edit_value(self.ui.list_widget_value.currentItem())
                elif action == del_action:
                    self.push_button_delite_data_click()
            else:
                some_action = context_menu.addAction('Добавить')
                action = context_menu.exec(self.ui.list_widget_value.mapToGlobal(pos))
                if action == some_action:
                    self.push_button_add_data_click()

    def __fill_combo_box_selection_data(self):
        self.ui.combo_box_selection_data.clear()
        for name in self.state.data.name():
            self.ui.combo_box_selection_data.addItem(
                name[1], name)

    def __fill_list_widget_answer(self):
        self.ui.list_widget_answer.clear()
        for answer in self.state.data.answer(self.ui.combo_box_selection_data.currentData()):
            if answer:
                _item = QListWidgetItem(str(answer[1]))
                _item.setFlags(_item.flags() & ~Qt.ItemIsSelectable)
                self.ui.list_widget_answer.addItem(_item)

    def __set_answer(self, answers):
        if answers is not None:
            for index, answer in enumerate(answers):
                try:
                    self.state.data.change_answer(
                        self.ui.combo_box_selection_data.currentData(),
                        index,
                        answer)
                except IndexError:
                    self.state.data.append_answer(
                        self.ui.combo_box_selection_data.currentData(),
                        answer)
            self.__fill_list_widget_answer()
            if self.ui.list_widget_answer.count() == 0:
                self.ui.line_edit_metod.setText(
                    'Грубых погрешностей не обнаружено')
            else:
                self.ui.line_edit_metod.setText(
                    f'Расчёт проведён методом {self.user_db.select_method(
                        self.settings.load_calculation().method.value + 1)}')
            self.state.save_data_mode = False
        else:
            self.ui.line_edit_metod.setText('Для данных неполучиловь найти значений')
        self.state.data.change_method(
            self.ui.combo_box_selection_data.currentData(),
            self.settings.load_calculation().method.value)

    def __set_method(self):
        self.__fill_list_widget_answer()
        if self.state.data.method(self.ui.combo_box_selection_data.currentData()):
            self.ui.line_edit_metod.setText(
                f'Расчёт проведён методом {self.user_db.select_method(
                    self.state.data.method(self.ui.combo_box_selection_data.currentData())
                )}')
        else:
            self.ui.line_edit_metod.setText(
                'Значения ещё не подсчитаны')
