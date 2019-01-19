from PyQt5.QtWidgets import QWidget

class TemplateModule(QWidget):
	def __init__ (self):
		__init__("Template Module", 10, 10)

	def __init__ (self, name, height, width):
		super(QWidget, self).__init__()
		self.name = name
		self.height = height
		self.width = width
