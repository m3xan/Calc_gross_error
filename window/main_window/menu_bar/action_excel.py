"""
Реакция на нажатие на action_excel
"""

import os
import ast

from PySide6.QtWidgets import QFileDialog

from thread.read_thred import ReadThread
from window.second_windows.load_window.load_window import LoadDialog

def action_excel_click(self) -> bool:
    """
    Реакция на нажатие на action_excel
    """
    filedialog = QFileDialog()
    self.state.excel_path = filedialog.getOpenFileName(caption='Выбрать файл',
                                                 dir=f'{os.path.join(os.getenv("userprofile"), "Desktop")}',
                                                 filter= 'Excel File (*.xlsx;*.xlsm;*.xltx;*.xltm)'
                                                )
    if self.state.excel_path != ('', ''):
        self.read_thread = ReadThread(self.state.excel_path[0])
        self.read_thread.start()
        self.read_thread.read_excel_signal.connect(self.on_change)
        self.window = LoadDialog()
        self.window.exec()
        return True
    return False

def on_change(self, read_excel_signal):
    """
    Костыль что бы ядро "ReadThread" реботало
    но не захломляло MainWindow
    """
    self.window.close()
    self.state.data = ast.literal_eval(read_excel_signal)
    if self.state.data is not None:
        self.ui.combo_box_selection_data.clear()
        for key in self.state.data:
            self.ui.combo_box_selection_data.addItem(
                                                    key[1],
                                                    key
                                                    )
