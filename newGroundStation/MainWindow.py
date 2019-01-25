#created by jwenner
#edited by jwenner

from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton
from Template import *

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.resize(800, 480) #Pi Screen Size
		self.setWindowTitle("New Ground Station @ Stratos")
		self.currentTemplate = Template(self)
		self.createSettings()
		self.show()
	
	def createSettings(self):
		# Create Buttons
		self.optionsButton = QPushButton("\u2261", self)
		self.optionsButton.move(760, 0)
		self.optionsButton.setFixedSize(40,40)
		font = self.optionsButton.font()
		font.setPointSize(30)
		self.optionsButton.setFont(font)
		#ToDo: Create Settings Menu and connect it
