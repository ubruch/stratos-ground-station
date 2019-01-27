#created by jwenner
#edited by jwenner

from PyQt5.QtWidgets import QPushButton

class StratosButton (QPushButton):
	def __init__(self, text, positionx, positiony, checkable, parent):
		super(StratosButton, self).__init__(text, parent)
		self.setFixedSize(40,40)
		font = self.font()
		font.setPointSize(30)
		font.setBold(True)
		self.setFont(font)
		self.setCheckable(checkable)
		self.move(positionx, positiony)
