# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration_window.ui'
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

class Ui_Registration(object):
    def setupUi(self, Registration):
        if not Registration.objectName():
            Registration.setObjectName(u"Registration")
        Registration.resize(295, 307)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Registration.sizePolicy().hasHeightForWidth())
        Registration.setSizePolicy(sizePolicy)
        Registration.setMinimumSize(QSize(295, 307))
        Registration.setMaximumSize(QSize(295, 307))
        self.centralwidget = QWidget(Registration)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.push_button_login = QPushButton(self.centralwidget)
        self.push_button_login.setObjectName(u"push_button_login")

        self.gridLayout.addWidget(self.push_button_login, 5, 1, 1, 1)

        self.line_edit_password_check = QLineEdit(self.centralwidget)
        self.line_edit_password_check.setObjectName(u"line_edit_password_check")
        self.line_edit_password_check.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_edit_password_check.sizePolicy().hasHeightForWidth())
        self.line_edit_password_check.setSizePolicy(sizePolicy1)
        self.line_edit_password_check.setMinimumSize(QSize(0, 35))
        self.line_edit_password_check.setMaximumSize(QSize(16777215, 30))
        self.line_edit_password_check.setContextMenuPolicy(Qt.NoContextMenu)
        self.line_edit_password_check.setAcceptDrops(False)
        self.line_edit_password_check.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.line_edit_password_check.setEchoMode(QLineEdit.Password)
        self.line_edit_password_check.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_edit_password_check.setDragEnabled(True)
        self.line_edit_password_check.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.line_edit_password_check.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.line_edit_password_check, 2, 0, 1, 2)

        self.push_button_fin_registration = QPushButton(self.centralwidget)
        self.push_button_fin_registration.setObjectName(u"push_button_fin_registration")

        self.gridLayout.addWidget(self.push_button_fin_registration, 5, 0, 1, 1)

        self.line_edit_login = QLineEdit(self.centralwidget)
        self.line_edit_login.setObjectName(u"line_edit_login")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_edit_login.sizePolicy().hasHeightForWidth())
        self.line_edit_login.setSizePolicy(sizePolicy2)
        self.line_edit_login.setMinimumSize(QSize(0, 35))
        self.line_edit_login.setMaximumSize(QSize(16777215, 30))
        self.line_edit_login.setContextMenuPolicy(Qt.NoContextMenu)
        self.line_edit_login.setAcceptDrops(False)
        self.line_edit_login.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.line_edit_login, 0, 0, 1, 2)

        self.label_error = QLabel(self.centralwidget)
        self.label_error.setObjectName(u"label_error")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_error.sizePolicy().hasHeightForWidth())
        self.label_error.setSizePolicy(sizePolicy3)
        self.label_error.setMinimumSize(QSize(0, 40))
        self.label_error.setAlignment(Qt.AlignCenter)
        self.label_error.setWordWrap(True)

        self.gridLayout.addWidget(self.label_error, 3, 0, 1, 2)

        self.line_edit_password_main = QLineEdit(self.centralwidget)
        self.line_edit_password_main.setObjectName(u"line_edit_password_main")
        sizePolicy1.setHeightForWidth(self.line_edit_password_main.sizePolicy().hasHeightForWidth())
        self.line_edit_password_main.setSizePolicy(sizePolicy1)
        self.line_edit_password_main.setMinimumSize(QSize(0, 35))
        self.line_edit_password_main.setMaximumSize(QSize(16777215, 30))
        self.line_edit_password_main.setContextMenuPolicy(Qt.NoContextMenu)
        self.line_edit_password_main.setAcceptDrops(False)
        self.line_edit_password_main.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.line_edit_password_main.setEchoMode(QLineEdit.Password)
        self.line_edit_password_main.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_edit_password_main.setDragEnabled(True)
        self.line_edit_password_main.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.line_edit_password_main.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.line_edit_password_main, 1, 0, 1, 2)

        Registration.setCentralWidget(self.centralwidget)

        self.retranslateUi(Registration)

        QMetaObject.connectSlotsByName(Registration)
    # setupUi

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(QCoreApplication.translate("Registration", u"MainWindow", None))
        self.push_button_login.setText(QCoreApplication.translate("Registration", u"\u0412\u0445\u043e\u0434", None))
        self.line_edit_password_check.setText("")
        self.line_edit_password_check.setPlaceholderText(QCoreApplication.translate("Registration", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.push_button_fin_registration.setText(QCoreApplication.translate("Registration", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044e", None))
        self.line_edit_login.setText("")
        self.line_edit_login.setPlaceholderText(QCoreApplication.translate("Registration", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_error.setText("")
        self.line_edit_password_main.setText("")
        self.line_edit_password_main.setPlaceholderText(QCoreApplication.translate("Registration", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

