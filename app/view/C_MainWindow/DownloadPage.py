# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloadPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DownloadPage(object):
    def setupUi(self, DownloadPage):
        DownloadPage.setObjectName("DownloadPage")
        DownloadPage.resize(715, 477)
        self.gridLayout = QtWidgets.QGridLayout(DownloadPage)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.cb_src = QtWidgets.QComboBox(DownloadPage)
        self.cb_src.setObjectName("cb_src")
        self.gridLayout_5.addWidget(self.cb_src, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(DownloadPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.pb_update_fl = QtWidgets.QPushButton(DownloadPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_update_fl.sizePolicy().hasHeightForWidth())
        self.pb_update_fl.setSizePolicy(sizePolicy)
        self.pb_update_fl.setObjectName("pb_update_fl")
        self.gridLayout_5.addWidget(self.pb_update_fl, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(DownloadPage)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.pb_gp = QtWidgets.QProgressBar(self.groupBox)
        self.pb_gp.setProperty("value", 24)
        self.pb_gp.setObjectName("pb_gp")
        self.gridLayout_2.addWidget(self.pb_gp, 2, 1, 1, 1)
        self.pb_sp = QtWidgets.QProgressBar(self.groupBox)
        self.pb_sp.setProperty("value", 24)
        self.pb_sp.setObjectName("pb_sp")
        self.gridLayout_2.addWidget(self.pb_sp, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.l_speed = QtWidgets.QLabel(self.groupBox)
        self.l_speed.setObjectName("l_speed")
        self.gridLayout_2.addWidget(self.l_speed, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(DownloadPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.l_name = QtWidgets.QLabel(self.groupBox_2)
        self.l_name.setObjectName("l_name")
        self.gridLayout_3.addWidget(self.l_name, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.l_size = QtWidgets.QLabel(self.groupBox_2)
        self.l_size.setObjectName("l_size")
        self.gridLayout_3.addWidget(self.l_size, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 4, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_3 = QtWidgets.QGroupBox(DownloadPage)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lw_file_l = QtWidgets.QListWidget(self.groupBox_3)
        self.lw_file_l.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.lw_file_l.setAutoScroll(True)
        self.lw_file_l.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lw_file_l.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lw_file_l.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lw_file_l.setFlow(QtWidgets.QListView.TopToBottom)
        self.lw_file_l.setObjectName("lw_file_l")
        self.gridLayout_7.addWidget(self.lw_file_l, 1, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.le_search_fl = QtWidgets.QLineEdit(self.groupBox_3)
        self.le_search_fl.setInputMask("")
        self.le_search_fl.setObjectName("le_search_fl")
        self.gridLayout_6.addWidget(self.le_search_fl, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)
        self.pb_search_fl = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_search_fl.setObjectName("pb_search_fl")
        self.gridLayout_6.addWidget(self.pb_search_fl, 0, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.lw_file_l.raise_()
        self.lw_file_l.raise_()
        self.lw_file_l.raise_()
        self.gridLayout_8.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(DownloadPage)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lw_down_l = QtWidgets.QListWidget(self.groupBox_4)
        self.lw_down_l.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.lw_down_l.setAutoScroll(True)
        self.lw_down_l.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lw_down_l.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lw_down_l.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lw_down_l.setFlow(QtWidgets.QListView.TopToBottom)
        self.lw_down_l.setObjectName("lw_down_l")
        self.gridLayout_9.addWidget(self.lw_down_l, 4, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pb_clear_dl = QtWidgets.QPushButton(self.groupBox_4)
        self.pb_clear_dl.setObjectName("pb_clear_dl")
        self.gridLayout_11.addWidget(self.pb_clear_dl, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_4, 0, 8, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pb_add_dl = QtWidgets.QPushButton(DownloadPage)
        self.pb_add_dl.setObjectName("pb_add_dl")
        self.gridLayout_10.addWidget(self.pb_add_dl, 0, 0, 1, 1)
        self.pb_drop_dl = QtWidgets.QPushButton(DownloadPage)
        self.pb_drop_dl.setObjectName("pb_drop_dl")
        self.gridLayout_10.addWidget(self.pb_drop_dl, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 2, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_8, 1, 0, 1, 1)

        self.retranslateUi(DownloadPage)
        QtCore.QMetaObject.connectSlotsByName(DownloadPage)

    def retranslateUi(self, DownloadPage):
        _translate = QtCore.QCoreApplication.translate
        DownloadPage.setWindowTitle(_translate("DownloadPage", "DownloadPage"))
        self.label.setText(_translate("DownloadPage", "Source:"))
        self.pb_update_fl.setText(_translate("DownloadPage", "UpdateFileList"))
        self.groupBox.setTitle(_translate("DownloadPage", "Download Info"))
        self.label_2.setText(_translate("DownloadPage", "Single Progress:"))
        self.label_3.setText(_translate("DownloadPage", "Global Progress:"))
        self.label_8.setText(_translate("DownloadPage", "Speed:"))
        self.l_speed.setText(_translate("DownloadPage", "Unknown"))
        self.groupBox_2.setTitle(_translate("DownloadPage", "File Info"))
        self.l_name.setText(_translate("DownloadPage", "Unknown"))
        self.label_4.setText(_translate("DownloadPage", "Name:"))
        self.label_6.setText(_translate("DownloadPage", "Size:"))
        self.l_size.setText(_translate("DownloadPage", "Unknown"))
        self.groupBox_3.setTitle(_translate("DownloadPage", "File List"))
        self.le_search_fl.setPlaceholderText(_translate("DownloadPage", "filename keyword"))
        self.label_5.setText(_translate("DownloadPage", "Search:"))
        self.pb_search_fl.setText(_translate("DownloadPage", "Search"))
        self.groupBox_4.setTitle(_translate("DownloadPage", "Download List"))
        self.pb_clear_dl.setText(_translate("DownloadPage", "Clear List"))
        self.pb_add_dl.setText(_translate("DownloadPage", "Add=>"))
        self.pb_drop_dl.setText(_translate("DownloadPage", "<=Drop"))

