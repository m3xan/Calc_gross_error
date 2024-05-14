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
from window.second_windows.add_window.add_window import AddDialog
from window.second_windows.settings.main_settings.setting_window import SettingsDialog
from window.second_windows.settings.method_window.method_dialog import MethodsDialog
from window.second_windows.load_window.load_window import LoadDialog
from window.second_windows.about_window.about_window import AboutDialog

from thread import ReadThread, SaveAsThread, SaveThread

from functions.calcul.calc import Calculator, Romanovsky, Charlier, Dixon
from functions.graph.graph import GraphicMaker
from functions.loger import Logger

from data_class.data import Data

class MainWindow(AbstractWindow):
    """
    class MainWindow
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.state = DataclassMainWindow(
            active_mod= None, # данное условие писать с использование math case
            save_data_mode= True,
            data= None,
            excel_path= None,
            change_mode= False,
            add_mod= False,
            clearance_level = self.user_db.select_user().clearance_level,
            auto_save_time= self.settings.load_category_json('auto_save'),
        )
        self.change_theme()

        self.__init_graph()
        if self.settings.load_category_json('auto_save')['switched']:
            self.__init_timer()

        if self.state.clearance_level > 1:
            Logger().change_logger(self.user_db.get_id(), logging.INFO)
        else:
            Logger().change_logger(self.user_db.get_id())

        self.__init_reaction()

    # menubar
    @Slot()
    def action_bd_click(self):
        """
        on action bd clicked
        """
        self.read_thread = ReadThread()
        self.read_thread.start()
        self.read_thread.read_signal.connect(self.on_change)
        self.load_window = LoadDialog()
        self.load_window.exec()
        # change
        self.state.active_mod = 'bd'
        return f'self.state.active_mod = {self.state.active_mod}, {self.state.data}'

    @Slot()
    def action_excel_click(self):
        """
        on excel bd clicked
        """
        filedialog = QFileDialog()
        self.state.excel_path = filedialog.getOpenFileName(
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
            # change
            try:
                self.timer.start(self.state.auto_save_time['time'])
            except AttributeError:
                logging.info('timer off')
            self.state.active_mod = 'excel'
            return self.state.active_mod, self.state.excel_path, self.state.data
        return None

    @Slot()
    def action_save_click(self):
        """
        on save data
        """
        match self.state.active_mod:
            case 'excel':
                self.save_tread = SaveThread(self.state.excel_path[0], self.state.data)
                self.save_tread.saved.connect(self.__set_data)
                self.save_tread.start()
                # change
                self.state.save_data_mode = True
                return self.state.save_data_mode
            case 'bd':
                self.save_tread = SaveThread(self.state.data)
                self.save_tread.saved.connect(self.__set_data)
                self.save_tread.start()
                self.state.save_data_mode = True
                return self.state.save_data_mode
        return None

    @Slot(Data)
    def __set_data(self, data: Data):
        self.save_tread.deleteLater()
        self.state.data = data

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
    def action_info_click(self):
        """
        Открывает окно "О нас"
        """
        dialog = AboutDialog()
        return dialog.exec()

    @Slot()
    @staticmethod
    def action_help_click(): # ДОДЕЛАНО
        """
        Открывает пользовательскую документацию
        """
        try:
            os.startfile(r'Документация\Докуметация пользовательская.docx')
            return True
        except FileNotFoundError as err:
            raise err

    @Slot()
    def action_new_click(self):
        """
        МБ переписать
        """
        dialog = AddDialog()
        dialog.full_data.connect(self.add_selection_data)
        return dialog.exec()

    @Slot()
    def action_save_as_click(self):
        """
        on save_as clicked
        """
        if self.state.data:
            file_name = QFileDialog.getSaveFileName(
            self,
            'Сохранить как:',
            f'{os.path.join(os.getenv("userprofile"), f'Измерения {datetime.now().strftime('%d-%m-%Y %H.%M.%S')}')}',
            filter= "Книга Excel (*.xlsx)"
            )
            if file_name != ('', ''):
                self.save_as_thread = SaveAsThread(file_name[0], self.state.data)
                self.save_as_thread.start()
                return True
        return None

    @Slot()
    def action_setting_window_click(self):
        """
        open satting_widow
        """
        setting_widow = SettingsDialog()
        setting_widow.windowThemeChanged.connect(self.__update_ui)
        return setting_widow.exec()

    @Slot()
    def action_delite_click(self):
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
        return f'self.state.save_data_mode = {self.state.save_data_mode}'

    @Slot()
    def action_calc_click(self):
        dialog = MethodsDialog()
        return dialog.exec()

    # button
    @Slot()
    def push_button_create_graph_click(self):
        """
        Create graph
        """
        if not self.state.data:
            return False
        self.plt_tool_bar.update()
        self.canvbar.ax.clear()
        hist = [
            data[1] for data in self.state.data[self.ui.combo_box_selection_data.currentData()][0]
        ]
        n, bins, _ = self.canvbar.ax.hist(hist, rwidth=0.8, color='#ff8921', label= 'Распределение')
        bin_centers = 0.5 * (bins[:-1] + bins[1:])

        window_size = 5  # Размер окна для усреднения, можно добавить изменение в настройки измерения
        weights = np.ones(window_size) / window_size  # Веса для усреднения значений
        smoothed_hist = np.convolve(n, weights, mode='same')  # Применение усреднения по скользящему окну

        aligned_bin_centers = bin_centers[:len(smoothed_hist)]
        self.canvbar.ax.plot(aligned_bin_centers, smoothed_hist, '-o', label='Прямая распределения')

        settings = self.settings.load_canvas()
        self.canvbar.update_collor(
            settings['canvas'],
            settings['text']
        )
        self.canvbar.ax.legend()
        self.canvbar.draw()
        return True

    @Slot()
    def _push_button_create_calc_click(self):
        """
        create_calc
        """
        user_settings = self.settings.load_category_json('calculation')
        calculator = Calculator()
        match user_settings['method']:
            case 0:
                calculator.method = Romanovsky()
            case 1:
                calculator.method = Charlier()
            case 2:
                calculator.method = Dixon()

        answers = calculator.calculate_with(
            [data[1] for data in self.state.data.value(
                self.ui.combo_box_selection_data.currentData()
                )
            ],
            user_settings['significance_level']
        )
        self.__set_answer(answers)
        return f'self.state.save_data_mode = {self.state.save_data_mode}'

    @Slot()
    def push_button_add_data_click(self):# ПЕРЕДЕЛАТЬ
        """
        add data
        """
        self.add_item()
        self.state.save_data_mode = False

        return f'self.state.save_data_mode = {self.state.save_data_mode}'

    @Slot()
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
                        current_index
                    )
                    self.state.save_data_mode = False
                return f'self.state.save_data_mode = {self.state.save_data_mode}'
        return None

    @Slot(Data)
    def on_change(self, read_signal: Data):
        """
        заглушка
        """
        self.load_window.close()
        self.state.data = read_signal
        self.read_thread.quit()
        if self.state.data:
            self.ui.combo_box_selection_data.clear()
            for key in self.state.data.name():
                self.ui.combo_box_selection_data.addItem(
                    key[1],
                    key
                )
        self.state.data.set_metadate(True)
        self.fill_listwidget()
        self.enable_ui(True)

    # __init__
    def __init_graph(self):
        """
        заглушка
        """
        graphic_maker = GraphicMaker()
        settings = self.settings.load_canvas()
        self.canvbar = graphic_maker.empty_with_axes(
            color_text= settings['text'],
            color_fig= settings['canvas']
        )

        self.graphwindow = GraphWindow()
        self.plt_tool_bar = NavigationToolbar2QT(self.canvbar)
        self.graphwindow.graph.toolBar.insertWidget(self.graphwindow.graph.action_create_graph, self.plt_tool_bar)
        self.graphwindow.setCentralWidget(self.canvbar)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.insertWidget(0, self.graphwindow)

        self.ui.frame.setLayout(layout)

    def __init_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.action_save_click)

    def __init_main_list_widget_value(self):
        self.ui.list_widget_value.itemDoubleClicked.connect(self.edit_value)
        self.ui.list_widget_value.itemDoubleClicked.connect(self.change_stat)
        self.ui.list_widget_value.customContextMenuRequested.connect(self.__start_menu)

    def __init_main_combobox(self):
        self.ui.combo_box_selection_data.currentIndexChanged.connect(self.set_val_answer)

    def __init_main_button(self):
        self.ui.push_button_create_calc.clicked.connect(self._push_button_create_calc_click)
        self.ui.push_button_add_data.clicked.connect(self.push_button_add_data_click)
        self.ui.push_button_delite_data.clicked.connect(self.push_button_delite_data_click)

    def __init_main_action(self):
        self.ui.action_new.triggered.connect(self.action_new_click)
        self.ui.action_excel.triggered.connect(self.action_excel_click)
        self.ui.action_bd.triggered.connect(self.action_bd_click)
        self.ui.action_save.triggered.connect(self.action_save_click)
        self.ui.action_save_as.triggered.connect(self.action_save_as_click)
        self.ui.action_esc.triggered.connect(self.action_esc_click)
        self.ui.action_setting_window.triggered.connect(self.action_setting_window_click)
        self.ui.action_calc.triggered.connect(self.action_calc_click)
        self.ui.action_help.triggered.connect(self.action_help_click)
        self.ui.action_info.triggered.connect(self.action_info_click)
        self.ui.action_delite.triggered.connect(self.action_delite_click)

    def __init_graph_menubar(self):
        self.graphwindow.graph.action_create_graph.triggered.connect(self.push_button_create_graph_click)

    def __init_reaction(self):
        self.__init_graph_menubar()
        self.__init_main_action()
        self.__init_main_button()
        self.__init_main_combobox()
        self.__init_main_list_widget_value()

    # helpfull
    def __update_ui(self):
        self.change_theme()
        setting_canvas = self.settings.load_canvas()
        setting_window = self.settings.load_category_json('window')

        self.graphwindow.addToolBar(
            eval(setting_window['toolBar']),
            self.graphwindow.graph.toolBar
        )
        self.addDockWidget(
            eval(setting_window['dockWidget']),
            self.ui.dockWidget
        )
        self.canvbar.update_collor(
            setting_canvas['canvas'],
            setting_canvas['text']
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
            item.setFlags(item.flags() | Qt.ItemIsEditable)  # Добавляем возможность редактирования значения
            self.ui.list_widget_value.addItem(item)
            # Выделяем новый элемент и запускаем его редактирование
            self.edit_value(item)

    def closeEvent(self, event):
        """
        заглушка
        """
        self.__save_settings()
        logging.info('main window close')
        event.accept()  # Подтверждаем закрытие окна

    def __save_settings(self):
        """
        заглушка
        """
        try:
            self.settings.save_data_json(
                'window',
                f'Qt.{str(self.graphwindow.toolBarArea(self.graphwindow.graph.toolBar))[12:]}',
                'toolBar'
            )
            self.settings.save_data_json(
                'window',
                f'Qt.{str(self.dockWidgetArea(self.ui.dockWidget))[15:]}',
                'dockWidget')
            self.settings.save_start(
                self.user_db.select_user().username
            )
            logging.info('save settings')
            return True
        except FileNotFoundError as err:
            logging.error(err, exc_info= True)
            return False

    def fill_listwidget(self): # ПЕРЕСМОРЕТЬ ЧТО МОЖНО УПРОСТИТЬ
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

    def set_val_answer(self):
        self.fill_listwidget()
        self.set_method()

    def add_selection_data(self, full_data): #TODO ПЕРЕСМОТЕРТЬ
        """
        заглушка
        """
        # ПЕРЕПИСАТЬ ВСЮ ФУНКЦИ
        self.state.data += full_data
        self.__fill_combo_box_selection_data()
        self.enable_ui(True)
        self.state.save_data_mode = False

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

    def save_value(self, item, index, edit: QLineEdit):
        """
        заглушка
        """
        new_value = edit.text()
        # Проверяем, заполнено ли новое значение
        # TODO проверка на валидность данных
        if new_value == '':
            return

        self.ui.list_widget_value.takeItem(index)
        item.setText(str(float(new_value)))
        self.ui.list_widget_value.insertItem(index, item)
        if self.state.change_mode:
            self.state.data.change_value(
                self.ui.combo_box_selection_data.currentData(),
                index,
                float(new_value)
            )
        else:
            self.state.data.append_value(
                self.ui.combo_box_selection_data.currentData(),
                float(new_value)
            )
        edit.deleteLater()

        self.state.add_mod = False
        self.state.save_data_mode = False

    def change_stat(self):
        """
        заглушка
        """
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
                    self.change_stat()
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
        for key in self.state.data.name():
            self.ui.combo_box_selection_data.addItem(
                key[1],
                key
            )

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
                    answer
                    )
                except IndexError:
                    self.state.data.append_answer(
                        self.ui.combo_box_selection_data.currentData(),
                        answer
                    )
            self.__fill_list_widget_answer()
            if self.ui.list_widget_answer.count() == 0:
                self.ui.line_edit_metod.setText(
                    'Грубых погрешностей не обнаружено'
                )
            else:
                self.ui.line_edit_metod.setText(
                    f'Расчёт проведён методом {self.user_db.select_method(
                        self.settings.load_attribute('calculation', 'method') + 1
                    )}'
                )
            self.state.save_data_mode = False
        else:
            self.ui.line_edit_metod.setText('Для данных неполучиловь найти значений')
        self.state.data.change_method(
            self.ui.combo_box_selection_data.currentData(),
            self.settings.load_attribute('calculation', 'method') + 1
        )
    def set_method(self):
        self.__fill_list_widget_answer()
        if self.state.data.method(self.ui.combo_box_selection_data.currentData()):
            self.ui.line_edit_metod.setText(
                f'Расчёт проведён методом {self.user_db.select_method(
                    self.state.data.method(self.ui.combo_box_selection_data.currentData())
                )}'
            )
        else:
            self.ui.line_edit_metod.setText(
                'Значения ещё не подсчитаны'
            )
