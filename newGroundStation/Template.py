#created by jwenner
#edited by jwenner

from SensorView import *
from PyQt5.QtWidgets import QWidget
class Template(QWidget):
	widgetList = []
	
	def __init__(self, parent):
		super(Template, self).__init__(parent)
		#everything from here on is debug purpose
		self.addWidget(SensorView("Sensor 1", 200, 200, parent))
		self.addWidget(SensorView("Sensor 2", 200, 200, parent))
		self.widgetList[0].move(30, 30)
	
	def addWidget(self, widget):
		self.widgetList.append(widget)
