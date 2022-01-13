from ui import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import os

os.environ['DISPLAY'] = ':0'


class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



app = QtWidgets.QApplication([])

MainWindow = mainWindow()
MainWindow.setWindowTitle("Ismail & Mustafa Image Editor")
MainWindow.show()


sys.exit(app.exec_())
