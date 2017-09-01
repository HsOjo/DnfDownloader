# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsPage(object):
    def setupUi(self, SettingsPage):
        SettingsPage.setObjectName("SettingsPage")
        SettingsPage.resize(535, 415)
        self.gridLayout = QtWidgets.QGridLayout(SettingsPage)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(SettingsPage)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 2, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.le_dd = QtWidgets.QLineEdit(self.groupBox)
        self.le_dd.setObjectName("le_dd")
        self.gridLayout_3.addWidget(self.le_dd, 0, 1, 1, 1)
        self.tb_dd = QtWidgets.QToolButton(self.groupBox)
        self.tb_dd.setObjectName("tb_dd")
        self.gridLayout_3.addWidget(self.tb_dd, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.le_bs = QtWidgets.QLineEdit(self.groupBox)
        self.le_bs.setObjectName("le_bs")
        self.gridLayout_5.addWidget(self.le_bs, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 1, 1, 1, 1)
        self.pb_apply = QtWidgets.QPushButton(self.groupBox)
        self.pb_apply.setObjectName("pb_apply")
        self.gridLayout_2.addWidget(self.pb_apply, 3, 1, 1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(SettingsPage)
        QtCore.QMetaObject.connectSlotsByName(SettingsPage)

    def retranslateUi(self, SettingsPage):
        _translate = QtCore.QCoreApplication.translate
        SettingsPage.setWindowTitle(_translate("SettingsPage", "Form"))
        self.groupBox.setTitle(_translate("SettingsPage", "Download Settings"))
        self.label.setText(_translate("SettingsPage", "Down Directory"))
        self.tb_dd.setText(_translate("SettingsPage", "..."))
        self.label_2.setText(_translate("SettingsPage", "Download Block Size"))
        self.pb_apply.setText(_translate("SettingsPage", "Apply"))

