#created by jwenner
#edited by jwenner

#Superclass of all custom stratos widgets

from PyQt5.QtWidgets import QFrame
from PyQt5.QtGui import QPainter, QPalette, QColor, QFont
from PyQt5.QtCore import *

class TemplateModule(QFrame):
	def __init__(self, name, height, width):
		super(TemplateModule, self).__init__()
		self.name = name
		self.resize(height,width)
		#set basic custom look for all stratos ui elements
		self.setFrameShape(QFrame.StyledPanel)
		pal = QPalette()
		pal.setColor(QPalette.Background, Qt.lightGray)
		self.setAutoFillBackground(True)
		self.setPalette(pal)

	#Override paintEvent to display custom Content
	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		painter.setPen(Qt.black)
		font = QFont("Decorative", 15)
		font.setBold(True)
		painter.setFont(font)
		painter.drawText(event.rect(), Qt.AlignLeft, self.name)
		QFrame.paintEvent(self,event)
