#created by jwenner
#edited by jwenner

from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton
import Template
from Settings import *
from StratosButton import *

#Displayed window with settings Menu etcs
class MainWindow(QMainWindow):
	templateList = []
	
	def __init__(self):
		super(MainWindow, self).__init__()
		self.resize(800, 480) #Pi Screen Size
		self.setWindowTitle("New Ground Station @ Stratos")
		self.addTemplate()
		self.currentTemplate = 0
		self.createSettings()
		self.show()
	
	# Helper function to create Settings Menu
	def createSettings(self):
		# Create Buttons
		self.optionsButton = StratosButton("\u2261", 760, 0, False, self)
		#ToDo: Create Settings Menu and connect it
		self.settingsMenu = Settings(self)
		self.optionsButton.clicked.connect(self.settingsMenu.show)
		self.settingsMenu.tempAddButton.clicked.connect(self.addTemplate)
		self.settingsMenu.tempDelButton.clicked.connect(self.delTemplate)
		self.settingsMenu.nextTempButton.clicked.connect(self.nextTemplate)
		self.settingsMenu.prevTempButton.clicked.connect(self.prevTemplate)
	
	def addTemplate(self):
		self.templateList.append(Template(self))
	
	def delTemplate(self):
		if(len(self.templateList) >= 1):
			self.templateList[len(self.templateList)-1].__del__()
	
	def nextTemplate(self):
		if(self.currentTemplate + 1 < len(self.templateList)):
			self.templateList[self.currentTemplate].hide()
			self.currentTemplate = self.currentTemplate + 1
			self.templateList[self.currentTemplate].show()
			
	
	def prevTemplate(self):
		if(self.currentTemplate - 1 > 0):
			self.templateList[self.currentTemplate].hide()
			self.currentTemplate = self.currentTemplate - 1
			self.templateList[self.currentTemplate].show()
			
