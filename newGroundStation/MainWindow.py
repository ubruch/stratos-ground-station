from PyQt5.QtWidgets import QApplication, QLabel

class MainWindow:
	def __init__ (self):
		self.app = QApplication([])
		self.label = QLabel("Test")
		self.label.show()
		self.app.exec_()
