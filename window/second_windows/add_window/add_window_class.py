# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
from window.main_window import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(380, 403)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(380, 360))
        Dialog.setMaximumSize(QSize(1920, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.list_widget = QListWidget(Dialog)
        self.list_widget.setObjectName(u"list_widget")

        self.gridLayout.addWidget(self.list_widget, 3, 2, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.push_button_delite_data = QPushButton(Dialog)
        self.push_button_delite_data.setObjectName(u"push_button_delite_data")
        self.push_button_delite_data.setMinimumSize(QSize(150, 30))
        self.push_button_delite_data.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.push_button_delite_data)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 2, 1, 3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.line_edit_name = QLineEdit(Dialog)
        self.line_edit_name.setObjectName(u"line_edit_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_edit_name.sizePolicy().hasHeightForWidth())
        self.line_edit_name.setSizePolicy(sizePolicy2)
        self.line_edit_name.setText(u"")

        self.gridLayout_2.addWidget(self.line_edit_name, 1, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setLayoutDirection(Qt.RightToLeft)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 2, 1, 3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.push_button_ok = QPushButton(Dialog)
        self.push_button_ok.setObjectName(u"push_button_ok")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(55)
        sizePolicy4.setHeightForWidth(self.push_button_ok.sizePolicy().hasHeightForWidth())
        self.push_button_ok.setSizePolicy(sizePolicy4)
        self.push_button_ok.setMinimumSize(QSize(100, 30))
        self.push_button_ok.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.push_button_ok)

        self.horizontalSpacer = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.push_button_esc = QPushButton(Dialog)
        self.push_button_esc.setObjectName(u"push_button_esc")
        sizePolicy4.setHeightForWidth(self.push_button_esc.sizePolicy().hasHeightForWidth())
        self.push_button_esc.setSizePolicy(sizePolicy4)
        self.push_button_esc.setMinimumSize(QSize(100, 30))
        self.push_button_esc.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.push_button_esc)


        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 2, 1, 3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.push_button_delite_data.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442\u0441\u044f\n"
" \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438!", None))
        self.line_edit_name.setInputMask("")
        self.line_edit_name.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.push_button_ok.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0442\u0438", None))
        self.push_button_esc.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

