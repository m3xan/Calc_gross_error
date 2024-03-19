
from PySide6.QtWidgets import QLineEdit, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon

from window.second_windows.authorization_window.internal_window.login.login_window_class import Ui_Autorization
from window.data_class_for_window.dataclass import DataclassAutWindow
from window.abstract_model.models import AbstractWindow

from data_base.test_orm import autorisation
from data_base.test_orm import select_image
from data_base.models import User

from functions.settings.settings import load_theme
from functions.circle_image.circle_image import setCircleImage

class InternalAutorizationWindow(AbstractWindow):
    """Внутреннее окно авторизации"""
    registrarion:Signal = Signal(bool)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Autorization()
        self.ui.setupUi(self)

        self.state = DataclassAutWindow(
            theme= load_theme(self),
            standard_image= r'Data\Data_base\image\8hOlH9yPHi7DbakNO6XafkdRmjw3DANbj2ojvQqw.jpg'
        )
        # TODO add close_eye, open_eye
        self.close_eye = QIcon(':/button/free-icon-eye-4621498.png')
        self.open_eye = QIcon(':/button/free-icon-open-eye-829117.png')

        self.__init_show_button()
        self.__init_reaction()
        self.__set_image(self.state.standard_image)

    def __set_image(self, image_path):
        target_pixmap = setCircleImage(
            image_path,
            desired_size = self.ui.label_image.size().height()  # желаемый размер
        )
        self.ui.label_image.setPixmap(target_pixmap)

    def __init_show_button(self):
        self.show_button = QPushButton(self)
        self.show_button.setCursor(Qt.PointingHandCursor)
        self.show_button.setStyleSheet("border: none; padding: 0;")
        self.show_button.setIcon(self.open_eye)

        layout = QHBoxLayout(self.ui.line_edit_password)
        layout.setContentsMargins(9, -1, 26, -1)
        layout.addWidget(self.show_button, 0, Qt.AlignRight)

    def __init_reaction(self):
        self.ui.push_button_login.clicked.connect(self.__ckick)
        self.ui.line_edit_login.editingFinished.connect(self.__load_image)
        self.show_button.clicked.connect(self.__password_visibility)
        self.ui.push_button_registration.clicked.connect(self.__set_signall)

    def __set_signall(self):
        self.registrarion.emit(True)

    def __password_visibility(self):
        if self.ui.line_edit_password.echoMode() == QLineEdit.Password:
            self.ui.line_edit_password.setEchoMode(QLineEdit.Normal)
            self.show_button.setIcon(self.close_eye)
        else:
            self.ui.line_edit_password.setEchoMode(QLineEdit.Password)
            self.show_button.setIcon(self.open_eye)

    def __ckick(self):
        if self.ui.line_edit_password.text() != '':
            user_id = autorisation(
                self.ui.line_edit_login.text(),
                self.ui.line_edit_password.text()
            )
            if user_id is not None:
                self.change_theme(user_id)
                return user_id
            return 'Неверный логин или пароль'
        return None

    def __load_image(self):
        if self.ui.line_edit_login.text() != '':
            user: User = select_image(self.ui.line_edit_login.text())
            if user is not None:
                self.state.theme = load_theme(self, user.id)
                self.setWindowTitle(str(user.id))
                self.__set_image(user.image)

    def __str__(self) -> str:
        return self.state.__str__()
