# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_Autorization(object):
    def setupUi(self, Autorization):
        if not Autorization.objectName():
            Autorization.setObjectName(u"Autorization")
        Autorization.resize(295, 307)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Autorization.sizePolicy().hasHeightForWidth())
        Autorization.setSizePolicy(sizePolicy)
        Autorization.setMinimumSize(QSize(295, 307))
        Autorization.setMaximumSize(QSize(295, 307))
        self.centralwidget = QWidget(Autorization)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_image = QLabel(self.centralwidget)
        self.label_image.setObjectName(u"label_image")
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setMinimumSize(QSize(277, 177))
        self.label_image.setMaximumSize(QSize(16777215, 16777215))
        self.label_image.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_image, 0, 0, 1, 2)

        self.line_edit_login = QLineEdit(self.centralwidget)
        self.line_edit_login.setObjectName(u"line_edit_login")
        sizePolicy.setHeightForWidth(self.line_edit_login.sizePolicy().hasHeightForWidth())
        self.line_edit_login.setSizePolicy(sizePolicy)
        self.line_edit_login.setMinimumSize(QSize(277, 35))
        self.line_edit_login.setMaximumSize(QSize(16777215, 30))
        self.line_edit_login.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.line_edit_login, 1, 0, 1, 2)

        self.line_edit_password = QLineEdit(self.centralwidget)
        self.line_edit_password.setObjectName(u"line_edit_password")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_edit_password.sizePolicy().hasHeightForWidth())
        self.line_edit_password.setSizePolicy(sizePolicy1)
        self.line_edit_password.setMinimumSize(QSize(0, 35))
        self.line_edit_password.setMaximumSize(QSize(16777215, 30))
        self.line_edit_password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.line_edit_password.setEchoMode(QLineEdit.Password)
        self.line_edit_password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_edit_password.setDragEnabled(True)
        self.line_edit_password.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.line_edit_password.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.line_edit_password, 2, 0, 1, 2)

        self.push_button_login = QPushButton(self.centralwidget)
        self.push_button_login.setObjectName(u"push_button_login")

        self.gridLayout.addWidget(self.push_button_login, 3, 0, 1, 1)

        self.push_button_registration = QPushButton(self.centralwidget)
        self.push_button_registration.setObjectName(u"push_button_registration")

        self.gridLayout.addWidget(self.push_button_registration, 3, 1, 1, 1)

        Autorization.setCentralWidget(self.centralwidget)

        self.retranslateUi(Autorization)

        QMetaObject.connectSlotsByName(Autorization)
    # setupUi

    def retranslateUi(self, Autorization):
        Autorization.setWindowTitle(QCoreApplication.translate("Autorization", u"MainWindow", None))
        self.label_image.setText("")
        self.line_edit_login.setText("")
        self.line_edit_login.setPlaceholderText(QCoreApplication.translate("Autorization", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.line_edit_password.setText("")
        self.line_edit_password.setPlaceholderText(QCoreApplication.translate("Autorization", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.push_button_login.setText(QCoreApplication.translate("Autorization", u"\u0412\u0445\u043e\u0434", None))
        self.push_button_registration.setText(QCoreApplication.translate("Autorization", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

