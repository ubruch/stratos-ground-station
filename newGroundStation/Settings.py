#created by jwenner
#edited by jwenner

from PyQt5.QtWidgets import QFrame, QVBoxLayout
from PyQt5.QtGui import QPainter, QPalette, QColor, QFont
from PyQt5.QtCore import Qt
from StratosButton import *

class Settings(QFrame):
	def __init__(self, parent):
		super(Settings, self).__init__(parent)
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.move(740,0)
		self.setFixedSize(60,480)
		self.setFrameShape(QFrame.StyledPanel)
		pal = QPalette()
		pal.setColor(QPalette.Background, Qt.lightGray)
		self.setAutoFillBackground(True)
		self.setPalette(pal)
		self.createButtons()
		self.hide()
		
	def paintEvent(self, paintEvent):
		super(Settings, self).paintEvent(paintEvent)
		
	def createButtons(self):
		self.hideButton = StratosButton("X", 10,10, self)
		self.hideButton.clicked.connect(self.hide)
		self.moveButton = StratosButton("\u00BB", 10, 60, self)
		self.resizeButton = StratosButton("\u21F2", 10, 110, self)
		self.nextTempButton = StratosButton(">", 10, 160, self)
		self.prevTempButton = StratosButton("<", 10, 210, self)
		self.moduleAddButton = StratosButton("+", 10, 260, self)
		self.moduleDelButton = StratosButton("-", 10, 310, self)
		self.tempAddButton = StratosButton("+", 10, 360, self)
		self.tempDelButton = StratosButton("-", 10, 410, self)
