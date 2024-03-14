from PySide6.QtWidgets import QLineEdit, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon, QPixmap, QPainter, QRegion, QColor

from window.second_windows.authorization_window.internal_window.login.login_window_class import Ui_Autorization, QMainWindow
from window.data_class_for_window.dataclass import DataclassAutWindow

from data_base.test_orm import autorisation
from data_base.test_orm import select_image
from data_base.models import User

from settings.settings import load_theme

class InternalAutorizationWindow(QMainWindow):
    fin_aut:Signal = Signal(int)
    registrarion:Signal = Signal(bool)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Autorization()
        self.ui.setupUi(self)

        self.state = DataclassAutWindow(
            theme= load_theme(self),
            standard_image=r'Data\Data_base\image\8hOlH9yPHi7DbakNO6XafkdRmjw3DANbj2ojvQqw.jpg'
        )

        self.setCircleImage(self.state.standard_image)
        self.close_eye = QIcon(':/button/free-icon-eye-4621498.png')
        self.open_eye = QIcon(':/button/free-icon-open-eye-829117.png')

        self.__init_show_button()
        self.__init_reaction()

    def createCircleMask(self, size, x, y):
        mask = QPixmap(size, size)
        mask.fill(Qt.transparent)
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        # Центрируем круг внутри области
        painter.setBrush(QColor("black"))
        # Рисуем круг в центре своей области
        painter.drawEllipse(x, y, size, size)
        painter.end()
        region = QRegion(mask.mask())
        return region

    def setCircleImage(self, image_path):
        orig_pixmap = QPixmap(image_path)
        if not orig_pixmap.isNull():
            desired_size = self.ui.label_image.size().height()  # желаемый размер
            min_ = min(orig_pixmap.size().width(), orig_pixmap.size().height())
            if min_ == orig_pixmap.size().width():
                c = orig_pixmap.size().height() / orig_pixmap.size().width() * desired_size
                orig_pixmap = orig_pixmap.scaled(desired_size, c , Qt.KeepAspectRatio, Qt.SmoothTransformation)
                sx = 0
                sy = (orig_pixmap.size().height() - orig_pixmap.size().width()) /2
            else:
                c = orig_pixmap.size().width() / orig_pixmap.size().height() * desired_size
                orig_pixmap = orig_pixmap.scaled(c, desired_size , Qt.KeepAspectRatio, Qt.SmoothTransformation)
                sx = (orig_pixmap.size().width() - orig_pixmap.size().height()) /2
                sy = 0


            target_pixmap = QPixmap(desired_size, desired_size)
            target_pixmap.fill(Qt.transparent)

            painter = QPainter(target_pixmap)
            reg  = self.createCircleMask(desired_size, 0, 0)

            painter.setClipRegion(reg)

            painter.drawPixmap(0, 0, orig_pixmap, sx , sy, desired_size, desired_size)
            painter.end()
            self.ui.label_image.setPixmap(target_pixmap)


    def __init_show_button(self):

        self.show_button = QPushButton(self)
        self.show_button.setCursor(Qt.PointingHandCursor)
        self.show_button.setStyleSheet("border: none; padding: 0;")
        self.show_button.setIcon(self.close_eye)

        layout = QHBoxLayout(self.ui.line_edit_password)
        layout.setContentsMargins(9, -1, 26, -1)
        layout.addWidget(self.show_button, 0, Qt.AlignRight)

    def __init_reaction(self):
        self.ui.push_button_login.clicked.connect(self.__ckick)
        self.ui.line_edit_login.editingFinished.connect(self.__load_image)
        self.show_button.clicked.connect(self.__password_visibility)
        self.ui.push_button_registration.clicked.connect(self.set_signall)

    def set_signall(self):
        self.registrarion.emit(True)

    def __password_visibility(self):
        if self.ui.line_edit_password.echoMode() == QLineEdit.Password:
            self.ui.line_edit_password.setEchoMode(QLineEdit.Normal)
            self.show_button.setIcon(self.open_eye)
        else:
            self.ui.line_edit_password.setEchoMode(QLineEdit.Password)
            self.show_button.setIcon(self.close_eye)

    def __ckick(self):
        if self.ui.line_edit_password.text() != '':
            user_id = autorisation(
                self.ui.line_edit_login.text(),
                self.ui.line_edit_password.text()
            )
            if user_id is not None:
                self.fin_aut.emit(user_id)
                return user_id
            return 'Неверный логин или пароль'
        return None

    def __load_image(self):
        if self.ui.line_edit_login.text() != '':
            user: User = select_image(self.ui.line_edit_login.text())
            if user is not None:
                self.state.theme = load_theme(self, user.id)
                self.setCircleImage(user.image)
