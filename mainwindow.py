# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\wwwroot\Document\代码\Python\Qiniu Helper\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 498)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 471, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.tableWidget_Settings = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_Settings.setGeometry(QtCore.QRect(10, 20, 461, 131))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_Settings.setFont(font)
        self.tableWidget_Settings.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_Settings.setObjectName("tableWidget_Settings")
        self.tableWidget_Settings.setColumnCount(1)
        self.tableWidget_Settings.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_Settings.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_Settings.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_Settings.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_Settings.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_Settings.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_Settings.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_Settings.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_Settings.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_Settings.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_Settings.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_Settings.setItem(4, 0, item)
        self.tableWidget_Settings.horizontalHeader().setVisible(False)
        self.tableWidget_Settings.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Settings.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_Settings.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Settings.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Settings.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget_Settings.verticalHeader().setStretchLastSection(False)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(490, 10, 521, 411))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget_FileList = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_FileList.setGeometry(QtCore.QRect(10, 20, 511, 381))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_FileList.setFont(font)
        self.tableWidget_FileList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_FileList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_FileList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_FileList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_FileList.setObjectName("tableWidget_FileList")
        self.tableWidget_FileList.setColumnCount(3)
        self.tableWidget_FileList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_FileList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_FileList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_FileList.setHorizontalHeaderItem(2, item)
        self.tableWidget_FileList.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_FileList.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget_FileList.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_FileList.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_FileList.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_FileList.verticalHeader().setVisible(False)
        self.tableWidget_FileList.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_FileList.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget_FileList.verticalHeader().setSortIndicatorShown(True)
        self.pushButton_Lock = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Lock.setGeometry(QtCore.QRect(400, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Lock.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Lock.setIcon(icon1)
        self.pushButton_Lock.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Lock.setDefault(False)
        self.pushButton_Lock.setFlat(False)
        self.pushButton_Lock.setObjectName("pushButton_Lock")
        self.pushButton_CopyMD = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CopyMD.setEnabled(False)
        self.pushButton_CopyMD.setGeometry(QtCore.QRect(910, 420, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_CopyMD.setFont(font)
        self.pushButton_CopyMD.setObjectName("pushButton_CopyMD")
        self.pushButton_CopyLink = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CopyLink.setEnabled(False)
        self.pushButton_CopyLink.setGeometry(QtCore.QRect(830, 420, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_CopyLink.setFont(font)
        self.pushButton_CopyLink.setObjectName("pushButton_CopyLink")
        self.pushButton_Download = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Download.setEnabled(False)
        self.pushButton_Download.setGeometry(QtCore.QRect(760, 420, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Download.setFont(font)
        self.pushButton_Download.setObjectName("pushButton_Download")
        self.pushButton_Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Refresh.setEnabled(False)
        self.pushButton_Refresh.setGeometry(QtCore.QRect(680, 420, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Refresh.setFont(font)
        self.pushButton_Refresh.setObjectName("pushButton_Refresh")
        self.lineEdit_DragDrop = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_DragDrop.setEnabled(False)
        self.lineEdit_DragDrop.setGeometry(QtCore.QRect(20, 210, 461, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_DragDrop.setFont(font)
        self.lineEdit_DragDrop.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_DragDrop.setReadOnly(True)
        self.lineEdit_DragDrop.setObjectName("lineEdit_DragDrop")
        self.pushButton_ClipBoard = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ClipBoard.setEnabled(False)
        self.pushButton_ClipBoard.setGeometry(QtCore.QRect(380, 420, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_ClipBoard.setFont(font)
        self.pushButton_ClipBoard.setObjectName("pushButton_ClipBoard")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 23))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_GlobalSetting = QtWidgets.QAction(MainWindow)
        self.action_GlobalSetting.setObjectName("action_GlobalSetting")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.menu_File.addAction(self.action_GlobalSetting)
        self.menu_File.addAction(self.action_Exit)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Qiniu Helper - v1.0"))
        self.groupBox.setTitle(_translate("MainWindow", "参数设置"))
        item = self.tableWidget_Settings.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "*Access key"))
        item = self.tableWidget_Settings.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "*Secret key"))
        item = self.tableWidget_Settings.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "*空间名称(Bucket)"))
        item = self.tableWidget_Settings.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "*域名(Domain)"))
        item = self.tableWidget_Settings.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "文件前缀(Prefix)"))
        item = self.tableWidget_Settings.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "设定值"))
        __sortingEnabled = self.tableWidget_Settings.isSortingEnabled()
        self.tableWidget_Settings.setSortingEnabled(False)
        self.tableWidget_Settings.setSortingEnabled(__sortingEnabled)
        self.groupBox_2.setTitle(_translate("MainWindow", "文件列表"))
        self.tableWidget_FileList.setSortingEnabled(True)
        item = self.tableWidget_FileList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "文件名(key)"))
        item = self.tableWidget_FileList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "文件大小(fsize)"))
        item = self.tableWidget_FileList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "上传时间(putTime)"))
        self.pushButton_Lock.setText(_translate("MainWindow", "锁定"))
        self.pushButton_CopyMD.setText(_translate("MainWindow", "复制Markdown"))
        self.pushButton_CopyLink.setText(_translate("MainWindow", "复制外链"))
        self.pushButton_Download.setText(_translate("MainWindow", "下载"))
        self.pushButton_Refresh.setText(_translate("MainWindow", "刷新"))
        self.lineEdit_DragDrop.setText(_translate("MainWindow", "拖放文件自动上传或者点击按钮从剪贴板上传"))
        self.pushButton_ClipBoard.setText(_translate("MainWindow", "剪贴板上传"))
        self.menu_File.setTitle(_translate("MainWindow", "文件"))
        self.menu_Help.setTitle(_translate("MainWindow", "帮助"))
        self.action_GlobalSetting.setText(_translate("MainWindow", "全局设置"))
        self.action_About.setText(_translate("MainWindow", "关于"))
        self.action_Exit.setText(_translate("MainWindow", "退出"))

