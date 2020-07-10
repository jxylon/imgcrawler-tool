import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QDialog, QWidget

import crawler_func
import labelImg.labelImg as labelImg
import filter_ui
import settings_ui


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.crawler = crawler_func.Crawler()
        self.root_path = os.path.abspath('./') + '/'
        self.save_path = self.root_path
        self.cur_path = self.root_path
        self.pattern = 1
        self.thread_crawler = None
        self.thread_arrange = None
        self.isopen = False
        # ui函数
        self.filter_ui = filter_ui.Ui_MainWindow()
        self.filter_ui.setupUi(self.filter_ui)
        self.setting_ui = settings_ui.Ui_MainWindow()
        self.setting_ui.setupUi(self.setting_ui)
        self.lableimg_ui = labelImg.MainWindow(None, '../labelimg/data/predefined_classes.txt', None)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1000)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font2 = QtGui.QFont()
        font2.setFamily("微软雅黑")
        font2.setPointSize(11)
        font2.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_pattern = QtWidgets.QLabel(self.centralwidget)
        self.label_pattern.setObjectName("label_pattern")
        self.label_pattern.setFont(font2)
        self.verticalLayout.addWidget(self.label_pattern, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_website = QtWidgets.QLabel(self.centralwidget)
        self.label_website.setObjectName("label_website")
        self.label_website.setFont(font2)
        self.verticalLayout.addWidget(self.label_website, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_website = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_website.setObjectName("lineEdit_website")
        self.init_website_editor()
        self.verticalLayout.addWidget(self.lineEdit_website)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_keyword = QtWidgets.QLabel(self.centralwidget)
        self.label_keyword.setObjectName("label_keyword")
        self.label_keyword.setFont(font2)
        self.verticalLayout_2.addWidget(self.label_keyword, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_keyword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_keyword.setObjectName("lineEdit_keyword")
        self.verticalLayout_2.addWidget(self.lineEdit_keyword)
        spacerItem2 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setMaximum(self.crawler._page_num)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_2.setVisible(False)
        self.verticalLayout_2.addWidget(self.progressBar)
        self.verticalLayout_2.addWidget(self.progressBar_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_start.setStyleSheet("background-color:lightblue")
        self.pushButton_start.clicked.connect(self.start_onclick)
        self.verticalLayout_2.addWidget(self.pushButton_start)
        spacerItem3 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_tips = QtWidgets.QLabel(self.centralwidget)
        self.label_tips.setObjectName("label_tips")
        self.verticalLayout_2.addWidget(self.label_tips)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 25))
        self.menubar.setObjectName("menubar")
        self.menu_main = QtWidgets.QMenu(self.menubar)
        self.menu_main.setObjectName("menu_main")
        self.menu_function = QtWidgets.QMenu(self.menu_main)
        self.menu_function.setObjectName("menu_function")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_openfile = QtWidgets.QAction(MainWindow)
        self.action_openfile.setObjectName("action_openfile")
        self.action_openfile.setShortcut('Ctrl+O')
        self.action_openfile.triggered.connect(self.open_file)
        self.action_filter = QtWidgets.QAction(MainWindow)
        self.action_filter.setObjectName("action_filter")
        self.action_filter.setShortcut('Ctrl+F')
        self.action_filter.triggered.connect(self.filter_ui.showMaximized)
        self.action_arrange = QtWidgets.QAction(MainWindow)
        self.action_arrange.setObjectName("action_arrange")
        self.action_arrange.setShortcut('Ctrl+Shift+A')
        self.action_arrange.triggered.connect(self.on_arrange)
        self.action_setting = QtWidgets.QAction(MainWindow)
        self.action_setting.setObjectName("action_setting")
        self.action_setting.setShortcut('Ctrl+Shift+S')
        self.action_setting.triggered.connect(self.on_setting)
        self.action_stop = QtWidgets.QAction(MainWindow)
        self.action_stop.setObjectName("action_stop")
        self.action_stop.triggered.connect(self.on_stop)
        self.action_label = QtWidgets.QAction(MainWindow)
        self.action_label.setObjectName("action_label")
        self.action_label.setShortcut('Ctrl+L')
        self.action_label.triggered.connect(self.lableimg_ui.showMaximized)
        self.action_pattern1 = QtWidgets.QAction(MainWindow)
        self.action_pattern1.setCheckable(True)
        self.action_pattern1.setChecked(True)
        self.action_pattern1.setObjectName("action_pattern1")
        self.action_pattern1.triggered.connect(lambda: self.change_pattern(1))
        self.action_pattern2 = QtWidgets.QAction(MainWindow)
        self.action_pattern2.setObjectName("action_pattern2")
        self.action_pattern2.triggered.connect(lambda: self.change_pattern(2))
        self.menu_function.addAction(self.action_pattern1)
        self.menu_function.addSeparator()
        self.menu_function.addAction(self.action_pattern2)
        self.menu_main.addAction(self.action_openfile)
        self.menu_main.addSeparator()
        self.menu_main.addAction(self.menu_function.menuAction())
        self.menu_main.addSeparator()
        self.menu_main.addAction(self.action_filter)
        self.menu_main.addSeparator()
        self.menu_main.addAction(self.action_arrange)
        self.menu_main.addSeparator()
        self.menu_main.addAction(self.action_label)
        self.menu_main.addSeparator()
        self.menu_main.addAction(self.action_setting)
        self.menu_main.addSeparator()
        self.menu_main.addAction(self.action_stop)
        self.menubar.addAction(self.menu_main.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "imgcrawler"))
        self.init_pattern_label()
        self.label_website.setText(_translate("MainWindow", "网址"))
        self.label_keyword.setText(_translate("MainWindow", "关键词"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.progressBar_2.setFormat(_translate("MainWindow", "%v/%m"))
        self.pushButton_start.setText(_translate("MainWindow", "开始爬取"))
        self.label_tips.setText(_translate("MainWindow", "存储路径：" + self.root_path))
        self.menu_main.setTitle(_translate("MainWindow", "功能"))
        self.menu_function.setTitle(_translate("MainWindow", "模式"))
        self.action_openfile.setText(_translate("MainWindow", "更改存储路径"))
        self.action_filter.setText(_translate("MainWindow", "审核"))
        self.action_label.setText(_translate("MainWindow", "标注"))
        self.action_arrange.setText(_translate("MainWindow", "图片重命名"))
        self.action_stop.setText(_translate("MainWindow", "停止爬虫"))
        self.action_setting.setText(_translate("MainWindow", "设置"))
        self.action_pattern1.setText(_translate("MainWindow", "模式一：爬取百度图片"))
        self.action_pattern2.setText(_translate("MainWindow", "模式二：爬取网站所有图片"))

    # 功能函数
    def open_file(self):
        """
        更改存储路径

        """
        filename = QFileDialog.getExistingDirectory(caption='更改存储路径', directory=self.save_path)
        self.isopen = False
        if filename:
            self.save_path = filename + '/'
            self.filter_ui.cur_path = filename + '/'
            self.isopen = True
            self.label_tips.setText("当前存储路径：" + self.save_path)

    def get_cur_path(self):
        filename = QFileDialog.getExistingDirectory(caption='打开文件夹', directory=self.cur_path)
        self.isopen = False
        if filename:
            self.cur_path = filename + '/'
            self.isopen = True

    def init_website_editor(self):
        if self.pattern == 1:
            self.lineEdit_website.setText('http://image.baidu.com/')
            self.lineEdit_website.setFocusPolicy(QtCore.Qt.NoFocus)
        else:
            self.lineEdit_website.setText('http://')
            self.lineEdit_website.setFocusPolicy(QtCore.Qt.ClickFocus)

    def init_pattern_label(self):
        _translate = QtCore.QCoreApplication.translate
        pattern_name = ['模式一：爬取百度图片', '模式二：爬取网站所有图片']
        self.label_pattern.setText(_translate("MainWindow", pattern_name[self.pattern - 1]))

    def change_pattern(self, idx):
        if idx == 1:
            self.pattern = 1
            self.action_pattern1.setCheckable(True)
            self.action_pattern1.setChecked(True)
            self.action_pattern2.setChecked(False)
            self.progressBar_2.setMaximum(self.crawler._page_num)
        elif idx == 2:
            self.pattern = 2
            self.action_pattern1.setChecked(False)
            self.action_pattern2.setCheckable(True)
            self.action_pattern2.setChecked(True)
            self.progressBar_2.setMaximum(1)
        self.init_website_editor()
        self.init_pattern_label()

    def start_onclick(self):
        """
        开始爬取按钮函数
        """
        website = self.lineEdit_website.text()
        keyword = self.lineEdit_keyword.text()
        self.progressBar.setVisible(True)
        self.progressBar_2.setVisible(True)
        self.crawler._save_path = self.save_path
        # 停止线程使用
        self.crawler.flag = True
        # 用到了时间间隔、爬取页数，所以需要重新加载
        self.crawler.load_parameter()
        self.thread_crawler = Worker_crawler(self.pattern, self.crawler, keyword, website)
        self.thread_crawler.progressBarValue.connect(self.on_imgchange)
        self.thread_crawler.progressBarValue2.connect(self.on_pagechange)
        self.thread_crawler.start()

    def on_imgchange(self, i):
        self.progressBar.setValue(i)

    def on_pagechange(self, obj):
        self.progressBar_2.setValue(obj['val'])
        if obj['code'] == 2:
            QtWidgets.QMessageBox.information(self, "提示", "爬取完毕", QtWidgets.QMessageBox.Yes)
        elif obj['code'] == 3:
            QtWidgets.QMessageBox.information(self, "提示", "停止线程完毕", QtWidgets.QMessageBox.Yes)

    def on_arrangechange(self, obj):
        self.progressBar.setValue(obj['val'])
        if obj['code'] == 2:
            QtWidgets.QMessageBox.information(self, "提示", "图片重命名完毕", QtWidgets.QMessageBox.Yes)

    def on_arrange(self):
        self.get_cur_path()
        # 用到了重命名后缀，重命名起始数字，所以需要重新加载
        self.crawler.load_parameter()
        if self.isopen:
            self.progressBar.setVisible(True)
            self.progressBar_2.setVisible(False)
            self.thread_arrange = Worker_arrange(self.crawler, self.cur_path)
            self.thread_arrange.progressBarValue.connect(self.on_arrangechange)
            self.thread_arrange.start()

    def on_stop(self):
        self.crawler.flag = False

    def on_setting(self):
        self.setting_ui.load_parameter()
        self.setting_ui.show()


class Worker_crawler(QThread):
    progressBarValue = pyqtSignal(int)  # 更新进度条
    progressBarValue2 = pyqtSignal(dict)

    def __init__(self, pattern, crawler, keyword, website):
        super(Worker_crawler, self).__init__()
        self.pattern = pattern
        self.crawler = crawler
        self.keyword = keyword
        self.website = website
        crawler.signal_img = self.progressBarValue
        crawler.signal_page = self.progressBarValue2

    def run(self):
        if self.pattern == 1:
            self.crawler.start_craw(1, self.keyword)
        elif self.pattern == 2:
            self.crawler.start_craw(2, _url=self.website)


class Worker_arrange(QThread):
    progressBarValue = pyqtSignal(dict)  # 更新进度条

    def __init__(self, crawler, path):
        super(Worker_arrange, self).__init__()
        self.crawler = crawler
        self.save_path = path
        self.crawler.signal_arrange = self.progressBarValue

    def run(self):
        self.crawler.arrange_imgname(self.save_path)
