#created by jwenner
#edited by jwenner

from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton
from Template import *
from Settings import *
from StratosButton import *

#Displayed window with settings Menu etcs
class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.resize(800, 480) #Pi Screen Size
		self.setWindowTitle("New Ground Station @ Stratos")
		self.currentTemplate = Template(self)
		self.createSettings()
		self.show()
	
	# Helper function to create Settings Menu
	def createSettings(self):
		# Create Buttons
		self.optionsButton = StratosButton("\u2261", 760, 0, False, self)
		#ToDo: Create Settings Menu and connect it
		self.settingsMenu = Settings(self)
		self.optionsButton.clicked.connect(self.settingsMenu.show)
