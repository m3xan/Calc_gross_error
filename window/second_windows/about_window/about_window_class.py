# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QSizePolicy, QVBoxLayout, QWidget)
from window.main_window import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(680, 224)
        Dialog.setMinimumSize(QSize(680, 224))
        Dialog.setMaximumSize(QSize(680, 224))
        icon = QIcon()
        icon.addFile(u":/info.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 661, 221))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setPixmap(QPixmap(u":/Hd-n8GFDUB0.jpg"))

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041e \u043d\u0430\u0441", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u0430\u043d\u0434\u0430 \u0432\u044f\u043b\u044b\u0439 \u043f\u0438\u0442\u043e\u043d \u0441 \u043f\u0440\u043e\u0435\u0442\u043e\u043c:\n"
"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432 \u043f\u0440\u044f\u043c\u044b\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u0439 \u043d\u0430 \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0445\n"
"\u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0435\u0439 \u0434\u043e\u043f\u0443\u0449\u0435\u043d\u043d\u044b\u0445 \u043d\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0435", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0412 \u0442\u0440\u0438 \u0441\u0442\u0440\u043e\u0447\u043a\u0438\n"
"\u041c\u043e\u0436\u043d\u043e \u0443\u043c\u0435\u0441\u0442\u0438\u0442\u044c \u0432\u0435\u0441\u044c \u043c\u0438\u0440.\n"
"Python \u044f\u0437\u044b\u043a \u043f\u0440\u0435\u043a\u0440\u0430\u0441\u043d\u044b\u0439.\n"
"\u00a9 Copyright: \u0421\u0435\u0440\u0433\u0435\u0439 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u043e\u0432\u0438\u0447 \u0415\u0444\u0438\u043c\u043e\u0432, 2014", None))
    # retranslateUi

