import mainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def add_directory():
    filename = QtWidgets.QFileDialog.getExistingDirectory()
    ui.listDir.addItem(str(filename))


app = QtWidgets.QApplication(sys.argv)
mWin = QtWidgets.QMainWindow()
ui = mainWindow.Ui_MainWindow()
ui.setupUi(mWin)
#mWin = uic.loadUi("mainwindow.ui")
ui.btnAddDir.clicked.connect(add_directory)

mWin.show()
sys.exit(app.exec_())
