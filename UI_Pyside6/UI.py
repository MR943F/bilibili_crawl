# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(668, 590)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_5.addWidget(self.pushButton_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(200, 100))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.radioButton = QRadioButton(self.tab)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMaximumSize(QSize(149, 19))
        self.radioButton.setChecked(True)

        self.horizontalLayout_23.addWidget(self.radioButton)

        self.label_16 = QLabel(self.tab)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(149, 19))

        self.horizontalLayout_23.addWidget(self.label_16)


        self.verticalLayout.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.radioButton_2 = QRadioButton(self.tab)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMaximumSize(QSize(149, 19))

        self.horizontalLayout_24.addWidget(self.radioButton_2)

        self.label_17 = QLabel(self.tab)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(149, 19))

        self.horizontalLayout_24.addWidget(self.label_17)


        self.verticalLayout.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.radioButton_3 = QRadioButton(self.tab)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMaximumSize(QSize(149, 19))

        self.horizontalLayout_25.addWidget(self.radioButton_3)

        self.label_18 = QLabel(self.tab)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(149, 19))

        self.horizontalLayout_25.addWidget(self.label_18)


        self.verticalLayout.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.radioButton_4 = QRadioButton(self.tab)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setMaximumSize(QSize(149, 19))

        self.horizontalLayout_26.addWidget(self.radioButton_4)

        self.label_37 = QLabel(self.tab)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(149, 19))

        self.horizontalLayout_26.addWidget(self.label_37)


        self.verticalLayout.addLayout(self.horizontalLayout_26)


        self.horizontalLayout_27.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout_27)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_9.addWidget(self.label_13)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_9.addWidget(self.label_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)


        self.verticalLayout_10.addLayout(self.verticalLayout_8)

        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_10.addWidget(self.pushButton_2)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.progressBar = QProgressBar(self.tab_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressBar)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.progressBar_2 = QProgressBar(self.tab_2)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(0)

        self.horizontalLayout_5.addWidget(self.progressBar_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_11.addLayout(self.verticalLayout_6)


        self.horizontalLayout_12.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_10.addWidget(self.label_14)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_10.addWidget(self.label_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)

        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)


        self.verticalLayout_12.addLayout(self.verticalLayout_9)

        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_12.addWidget(self.pushButton_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.progressBar_4 = QProgressBar(self.tab_2)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setValue(0)

        self.horizontalLayout_6.addWidget(self.progressBar_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.progressBar_3 = QProgressBar(self.tab_2)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setValue(0)

        self.horizontalLayout_7.addWidget(self.progressBar_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)


        self.verticalLayout_12.addLayout(self.verticalLayout_7)


        self.horizontalLayout_12.addLayout(self.verticalLayout_12)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u767b\u5f55\u4e8c\u7ef4\u7801", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u94fe\u63a5", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u5230\u4e0b\u8f7d\u5217\u8868", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u753b\u8d28\u9009\u62e9", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"1080", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"1", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"720", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"1", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"480", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"1", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"360", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u9996\u9875", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u6807\u9898\uff1a", None))
        self.label_3.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u94fe\u63a5\uff1a", None))
        self.label_5.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u97f3\u9891\u4e0b\u8f7d\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u4e0b\u8f7d\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u6807\u9898\uff1a", None))
        self.label_4.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u94fe\u63a5\uff1a", None))
        self.label_6.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u97f3\u9891\u4e0b\u8f7d\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u4e0b\u8f7d\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u4e0b\u8f7d", None))
    # retranslateUi

