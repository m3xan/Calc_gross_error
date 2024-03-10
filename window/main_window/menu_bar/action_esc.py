"""
Реакция на нажатие на action_esc
"""


from PySide6.QtWidgets import QMessageBox, QApplication

from excel import excel

def action_esc_click(self):
    """
    Заглушки QMessageBox
    сохронение в попок
    и есть close event

    ИСПРАВИТЬ
    ИСПРАВИТЬ
    ИСПРАВИТЬ
    
    """
    if self.state.save_data_mode is True:
        QApplication.closeAllWindows()
    else:
        result = QMessageBox.question(
            self,
            "Сохранить?",
            "Cохранить результат?",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No,
            defaultButton = QMessageBox.StandardButton.Ok
        )
        if result == QMessageBox.StandardButton.Ok:
            #  ДОПИЛИТЬ СОХРАНЕНИЕ
            if self.state.active_mod == 'excel':
                try:
                    excel.save_result_calc_excel(self.state.excel_path[0], self.state.data)
                    QApplication.closeAllWindows()
                except PermissionError as err:
                    return err
            elif self.state.active_mod == 'bd':
                try:
                    # save_bd TODO
                    QApplication.closeAllWindows()
                except FileNotFoundError:
                    ...

        elif result == QMessageBox.StandardButton.No:
            QApplication.closeAllWindows()
            return True
    return None
