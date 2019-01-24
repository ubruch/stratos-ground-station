#created by jwenner
#edited by jwenner

from PyQt5.QtWidgets import QMainWindow, QWidget
from Template import *

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.resize(800,480) #Pi Screen Size
		self.setWindowTitle("New Ground Station @ Stratos")
		self.centralWidget = QWidget()
		self.currentTemplate = Template()
		self.centralWidget.setLayout(self.currentTemplate)
		self.setCentralWidget(self.centralWidget)
		self.show()
