#created by jwenner
#edited by jwenner

from SensorView import *
from PyQt5.QtWidgets import QHBoxLayout, QLabel
class Template(QHBoxLayout):
	def __init__(self):
		super(QHBoxLayout, self).__init__()
		#everything from here on is debug purpose
		self.addWidget(SensorView("TestSensor",50,50))
		self.addWidget(SensorView("I am Widget 2",70,70))
		print("Created Layout")
