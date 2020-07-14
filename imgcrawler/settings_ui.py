# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.root_path = os.path.abspath('./')
        self.para_list = ['time_step', 'start_page', 'page_num', 'file_suffix', 'start_num']

    def load_parameter(self):
        with open(os.path.join(self.root_path, "settings.txt"), "r") as f:  # 打开文件
            lines = f.readlines()  # 按行读取文件
            for line in lines:  # 遍历每一行
                s = line.split('=')  # 按=分开参数和数值
                para, val = s[0], s[1]
                t = eval('self.lineEdit_' + para)
                t.setText(val.strip().strip('\''))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_file_suffix = QtWidgets.QLabel(self.centralwidget)
        self.label_file_suffix.setObjectName("label_file_suffix")
        self.horizontalLayout_5.addWidget(self.label_file_suffix)
        self.lineEdit_file_suffix = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_file_suffix.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_file_suffix.setObjectName("lineEdit_file_suffix")
        self.horizontalLayout_5.addWidget(self.lineEdit_file_suffix)
        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_time_step = QtWidgets.QLabel(self.centralwidget)
        self.label_time_step.setObjectName("label_time_step")
        self.horizontalLayout_3.addWidget(self.label_time_step)
        self.lineEdit_time_step = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_time_step.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_time_step.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_time_step.setObjectName("lineEdit_time_step")
        self.horizontalLayout_3.addWidget(self.lineEdit_time_step)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_start_num = QtWidgets.QLabel(self.centralwidget)
        self.label_start_num.setObjectName("label_start_num")
        self.horizontalLayout_9.addWidget(self.label_start_num)
        self.lineEdit_start_num = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_start_num.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_start_num.setObjectName("lineEdit_start_num")
        self.horizontalLayout_9.addWidget(self.lineEdit_start_num)
        self.gridLayout.addLayout(self.horizontalLayout_9, 8, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_start_page = QtWidgets.QLabel(self.centralwidget)
        self.label_start_page.setObjectName("label_start_page")
        self.horizontalLayout_6.addWidget(self.label_start_page)
        self.lineEdit_start_page = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_start_page.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_start_page.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_start_page.setObjectName("lineEdit_start_page")
        self.horizontalLayout_6.addWidget(self.lineEdit_start_page)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_page_num = QtWidgets.QLabel(self.centralwidget)
        self.label_page_num.setObjectName("label_page_num")
        self.horizontalLayout_4.addWidget(self.label_page_num)
        self.lineEdit_page_num = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_page_num.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_page_num.setObjectName("lineEdit_page_num")
        self.horizontalLayout_4.addWidget(self.lineEdit_page_num)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 7, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 9, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_save.setStyleSheet("background-color:lightblue")
        self.pushButton_save.clicked.connect(self.on_save)
        self.horizontalLayout_8.addWidget(self.pushButton_save)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.load_parameter()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_file_suffix.setText(_translate("MainWindow", "图片后缀名"))
        self.label_time_step.setText(_translate("MainWindow", "时间间隔"))
        self.label_start_num.setText(_translate("MainWindow", "重命名起始数字"))
        self.label_start_page.setText(_translate("MainWindow", "爬取起始页面"))
        self.label_page_num.setText(_translate("MainWindow", "爬取页数"))
        self.pushButton_save.setText(_translate("MainWindow", "保存"))

    def on_save(self):
        with open(os.path.join(self.root_path, "settings.txt"), "w+") as f:  # 打开文件
            for para in self.para_list:
                t = eval('self.lineEdit_' + para)
                v = t.text()
                if len(v.strip()) == 0:
                    v = '\'\''
                elif v and not v[0].isdigit():
                    v = '\'' + v + '\''
                f.write(para + '=' + v + '\n')
        QtWidgets.QMessageBox.information(self, "提示", "保存成功", QtWidgets.QMessageBox.Yes)

