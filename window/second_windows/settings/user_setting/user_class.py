# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(523, 168)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name_pass = QLabel(Dialog)
        self.label_name_pass.setObjectName(u"label_name_pass")
        self.label_name_pass.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_name_pass)

        self.linedit_username = QLineEdit(Dialog)
        self.linedit_username.setObjectName(u"linedit_username")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.linedit_username.sizePolicy().hasHeightForWidth())
        self.linedit_username.setSizePolicy(sizePolicy1)
        self.linedit_username.setMinimumSize(QSize(250, 0))
        self.linedit_username.setReadOnly(False)

        self.verticalLayout.addWidget(self.linedit_username)

        self.label_password = QLabel(Dialog)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_password)

        self.linedit_password = QLineEdit(Dialog)
        self.linedit_password.setObjectName(u"linedit_password")
        self.linedit_password.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.linedit_password)

        self.label_walidation_password = QLabel(Dialog)
        self.label_walidation_password.setObjectName(u"label_walidation_password")

        self.verticalLayout.addWidget(self.label_walidation_password)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.push_button_save = QPushButton(Dialog)
        self.push_button_save.setObjectName(u"push_button_save")
        sizePolicy1.setHeightForWidth(self.push_button_save.sizePolicy().hasHeightForWidth())
        self.push_button_save.setSizePolicy(sizePolicy1)
        self.push_button_save.setMinimumSize(QSize(80, 0))
        self.push_button_save.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.push_button_save)

        self.push_button_chose_image = QPushButton(Dialog)
        self.push_button_chose_image.setObjectName(u"push_button_chose_image")
        sizePolicy1.setHeightForWidth(self.push_button_chose_image.sizePolicy().hasHeightForWidth())
        self.push_button_chose_image.setSizePolicy(sizePolicy1)
        self.push_button_chose_image.setMinimumSize(QSize(118, 0))

        self.horizontalLayout_3.addWidget(self.push_button_chose_image)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.label_image = QLabel(Dialog)
        self.label_image.setObjectName(u"label_image")
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setMinimumSize(QSize(150, 150))

        self.horizontalLayout.addWidget(self.label_image)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_name_pass.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.label_password.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.linedit_password.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_walidation_password.setText("")
        self.push_button_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.push_button_chose_image.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443", None))
        self.label_image.setText("")
    # retranslateUi

