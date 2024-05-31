
from window.abstract_model.models import AbstractDialog

from .method_class import Ui_Mehod_dialog

class MethodsDialog(AbstractDialog):
    """
    Класс окна настроек интерфейса
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Mehod_dialog()
        self.ui.setupUi(self)
        self.change_theme()
        self.__start()

    def __start(self):
        self.__init_reaction()
        self.setstart()

    def __init_reaction(self):
        self.ui.push_button_next.clicked.connect(self.change_page)
        self.ui.push_button_back.clicked.connect(self.change_page)
        self.ui.push_button_save.clicked.connect(self.accept)
        self.ui.push_button_close.clicked.connect(self.reject)

    def setstart(self):
        data = self.settings.load_category_json('calculation')
        self.ui.tabWidget.setCurrentIndex(data['method'])
        self.__set_level(data['significance_level'])

    def __set_level(self, _p):
        match _p:
            case 0.99:
                self.ui.radio_button_099.setChecked(True)
            case 0.98:
                self.ui.radio_button_098.setChecked(True)
            case 0.95:
                self.ui.radio_button_095.setChecked(True)
            case 0.9:
                self.ui.radio_button_09.setChecked(True)

    def change_page(self):
        match self.ui.stackedWidget.currentIndex():
            case 0:
                self.ui.stackedWidget.setCurrentIndex(1)
                self.setWindowTitle('Выбор уровня значимости')
            case 1:
                self.ui.stackedWidget.setCurrentIndex(0)
                self.setWindowTitle('Выбор метода расчёта')
                
    def accept(self) -> None:
        data = {
            'method': self.ui.tabWidget.currentIndex(),
            'significance_level': self.__chesc_p()
        }
        self.settings.save_data_json('calculation', data)

        return super().accept()

    def __chesc_p(self) -> float:
        if self.ui.radio_button_099.isChecked():
            _p = 0.99
        if self.ui.radio_button_098.isChecked():
            _p = 0.98
        if self.ui.radio_button_095.isChecked():
            _p = 0.95
        if self.ui.radio_button_09.isChecked():
            _p = 0.9
        return _p
