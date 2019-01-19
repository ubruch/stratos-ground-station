from PyQt5.QtWidgets import QMainWindow
from Template import *

class MainWindow(QMainWindow):
	def __init__ (self):
		super(MainWindow, self).__init__()
		self.resize(800,480) #Pi Screen Size
		self.setWindowTitle("New Ground Station @ Stratos")
		self.currentTemplate = Template()
		self.show()
