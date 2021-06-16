import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append(os.path.realpath('.'))
from quiz import *
from db import *
from Worker import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())