# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authorization_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QMainWindow,
    QSizePolicy, QWidget)
from window.main_window import res_rc

class Ui_AuthorizationWindow(object):
    def setupUi(self, AuthorizationWindow):
        if not AuthorizationWindow.objectName():
            AuthorizationWindow.setObjectName(u"AuthorizationWindow")
        AuthorizationWindow.resize(295, 307)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AuthorizationWindow.sizePolicy().hasHeightForWidth())
        AuthorizationWindow.setSizePolicy(sizePolicy)
        AuthorizationWindow.setMinimumSize(QSize(295, 307))
        AuthorizationWindow.setMaximumSize(QSize(295, 307))
        icon = QIcon()
        icon.addFile(u":/icon/calculator-Freepik.png", QSize(), QIcon.Normal, QIcon.Off)
        AuthorizationWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(AuthorizationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        AuthorizationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AuthorizationWindow)

        QMetaObject.connectSlotsByName(AuthorizationWindow)
    # setupUi

    def retranslateUi(self, AuthorizationWindow):
        AuthorizationWindow.setWindowTitle(QCoreApplication.translate("AuthorizationWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
    # retranslateUi

