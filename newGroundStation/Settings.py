#created by jwenner
#edited by jwenner

from PyQt5.QtWidgets import QFrame, QVBoxLayout
from PyQt5.QtGui import QPainter, QPalette, QColor, QFont
from PyQt5.QtCore import Qt

class Settings(QFrame):
	def __init__(self, parent):
		super(Settings, self).__init__(parent)
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.move(740,0)
		self.setFixedSize(60,480)
		self.hide()
		self.setFrameShape(QFrame.StyledPanel)
		pal = QPalette()
		pal.setColor(QPalette.Background, Qt.lightGray)
		self.setAutoFillBackground(True)
		self.setPalette(pal)

	
	def paintEvent(self, paintEvent):
		super(Settings, self).paintEvent(paintEvent)
