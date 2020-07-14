import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import crawler_ui, settings_ui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = crawler_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
