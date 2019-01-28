#created by jwenner
#edited by jwenner

from SensorView import *
from PyQt5.QtWidgets import QWidget

#Container for Stratos UI elements
class Template(QWidget):
	widgetList = []
	
	def __init__(self, parent):
		super(Template, self).__init__(parent)
		#everything from here on is debug purpose
		self.addWidget(SensorView("Sensor 1", 200, 200, "NaN", self))
		self.addWidget(SensorView("Sensor 2", 200, 200, "NaN", self))
		self.widgetList[0].move(30, 30)
		self.resize(800, 480)
	
	def addWidget(self, widget):
		self.widgetList.append(widget)
		
	def hide(self):
		for i in self.widgetList:
			i.hide()
		super(Template, self).hide()
	
	def show(self):
		super(Template, self).show()
		for i in self.widgetList:
			i.show()
	
	def __del__(self):
		for i in self.widgetList:
			i.hide()
