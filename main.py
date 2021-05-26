import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
os.system('convertor.bat')
from mainMenu import *
from newGameAsk import *

class MyWin(QtWidgets.QMainWindow):

	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.backgroundLabel.setPixmap(QPixmap("pic/background.png"))

		self.ui.newGameAction.triggered.connect(self.newGameAsk)

	def newGameAsk(self):
		myask.show()

class NewGameAsk(QtWidgets.QMainWindow):

	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_NewGameAsk()
		self.ui.setupUi(self)

		self.ui.newGameNoBtn.clicked.connect(self.close)
		self.ui.newGameYeasBtn.clicked.connect(self.newGame)

	def newGame(self):
		self.close()
		TODO


if __name__=="__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyWin()

	ask = QtWidgets.QApplication(sys.argv)
	myask = NewGameAsk()

	myapp.show()
	sys.exit(app.exec())