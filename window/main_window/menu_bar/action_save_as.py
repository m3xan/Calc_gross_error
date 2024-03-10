import os
from datetime import datetime

from PySide6.QtWidgets import QFileDialog

from thread.save_as_excel_thread import SaveAsThread

def save_as_click(self):
    fileName = QFileDialog.getSaveFileName(None, 'Сохранить как:',
                                                f'{os.path.join(os.getenv("userprofile"),
                                                f'Измерения {str(datetime.now().strftime("%d-%m-%Y %H.%M.%S"))}')}',
                                                filter= """
                                                Книга Excel (*.xlsx);; 
                                                Книга Excel с поддержкой макросов(*.xlsm);; 
                                                Шаблон Excel(*.xltx);; 
                                                Шаблон Excel с поддержкой макросов (*.xltm)
                                                """
                                                )
    if fileName != ('', ''):
        self.save_as_thread = SaveAsThread(fileName[0], self.state.data)
        self.save_as_thread.start()
        return True
    return None
