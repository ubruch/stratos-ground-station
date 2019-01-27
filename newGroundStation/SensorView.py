#created by jwenner
#edited by jwenner

from TemplateModule import *
from PyQt5.QtWidgets import QHBoxLayout, QLabel

#Stratos custom View to display sensor data
class SensorView(TemplateModule):
	def __init__(self, name, width, height, reactsTo, parent):
		super(SensorView, self).__init__(name, width, height, parent)
		self.value = "No current Value"
		self.reactsTo = reactsTo
	
	#Override paintEvent to display custom Content
	def paintEvent(self, event):
		super(SensorView, self).paintEvent(event)
		painter = QPainter()
		painter.begin(self)
		painter.setPen(Qt.black)
		font = QFont("Decorative", 30)
		font.setBold(True)
		painter.setFont(font)
		painter.drawText(event.rect(), Qt.AlignCenter, self.value)
	
	#Function to add new value and trigger background flashing
	def addValue(self, value):
		self.value = value
		super(SensorView, self).flash()
