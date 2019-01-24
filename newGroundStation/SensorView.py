#created by jwenner
#edited by jwenner

from TemplateModule import *
from PyQt5.QtWidgets import QHBoxLayout, QLabel

class SensorView(TemplateModule):
	def __init__(self, name, width, height):
		super(SensorView, self).__init__(name,width,height)
		self.value = "No current Value"
	
	#Override paintEvent to display custom Content
	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		painter.setPen(Qt.black)
		font = QFont("Decorative", 30)
		font.setBold(True)
		painter.setFont(font)
		painter.drawText(event.rect(), Qt.AlignCenter, self.value)
		TemplateModule.paintEvent(self,event)
