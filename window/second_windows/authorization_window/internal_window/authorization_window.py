"""
тест
"""
from PySide6.QtWidgets import QLineEdit, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap

from window.main_window.main_window import MainWindow
from window.second_windows.authorization_window.authorization_window_class import QMainWindow, Ui_MainWindow
from window.data_class_for_window.dataclass import DataclassAutWindow
from data_base.user_hanler import autorisation
from data_base.user_hanler import select_image

from settings.settings import load_theme
from new_file.check_file import check_all_file


class AutWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.state = DataclassAutWindow(
            theme= load_theme(self),
            standard_image=r'Data\Data_base\image\8hOlH9yPHi7DbakNO6XafkdRmjw3DANbj2ojvQqw.jpg'
        )

        pixmap = QPixmap(self.state.standard_image).scaled(168,108, aspectMode=Qt.KeepAspectRatio)
        self.ui.label.setPixmap(pixmap)

        self.__init_show_button()
        self.__init_reaction()

    def __init_show_button(self):
        icon = QIcon()
        icon.addFile(":/save.png", QSize(), QIcon.Normal, QIcon.Off)

        self.show_button = QPushButton("Show", self)
        self.show_button.setCursor(Qt.PointingHandCursor)
        self.show_button.setStyleSheet("border: none; padding: 0;")
        self.show_button.setIcon(icon)

        layout = QHBoxLayout(self.ui.lineEdit_2)
        layout.setContentsMargins(9, -1, 26, -1)
        layout.addWidget(self.show_button, 0, Qt.AlignRight)

    def __init_reaction(self):
        self.ui.pushButton.clicked.connect(self.__ckick)
        self.ui.lineEdit.editingFinished.connect(self.__load_image)
        self.show_button.clicked.connect(self.__password_visibility)

    def __password_visibility(self):
        if self.ui.lineEdit_2.echoMode() == QLineEdit.Password:
            self.ui.lineEdit_2.setEchoMode(QLineEdit.Normal)
            self.show_button.setText("Hide")
        else:
            self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)
            self.show_button.setText("Show")

    def __ckick(self):
        if self.ui.lineEdit.text() != '':
            user_id = autorisation(
                self.ui.lineEdit.text(),
                self.ui.lineEdit_2.text()
            )
            if user_id:
                if check_all_file():
                    self.main_window = MainWindow(user_id)
                    self.main_window.show()
                    self.deleteLater()  # Удаление объекта после закрытия
                    return user_id
            return 'Неверный логин или пароль'
        return None

    def __load_image(self):
        if self.ui.lineEdit.text() != '':
            image_url, user = select_image(self.ui.lineEdit.text())
            self.state.theme = load_theme(self, user.id)
            pixmap = QPixmap(image_url).scaled(
                168, 108, aspectMode=Qt.KeepAspectRatio
            )
            self.ui.label.setPixmap(pixmap)
