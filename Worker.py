
from PyQt5 import QtCore, QtGui, QtWidgets
class Thread(QtCore.QThread):
    update_time = QtCore.pyqtSignal()
    def run(self):
       self.update_time.emit()