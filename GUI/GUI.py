import sys

from PyQt5.QtCore import QObject, pyqtSlot, QVariant
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

#planned functionalities:
#1. map; capable of moving, zooming, and showing: start, current location, and destination of the ballon 
# (map is added in qml, moving and zooming is working; start location is hard-coded atm)
#2. button and inputs to change start location (maybe with dropdown for locations that are used more than once)
#3. button and inputs to change destination
#4. maybe show stats like current flight time, local time, height of ballon etc


if __name__ == '__main__':
    myApp = QApplication(sys.argv)

    engine = QQmlApplicationEngine()
    context = engine.rootContext()
    context.setContextProperty("main", engine)

    engine.load('main.qml')

    win = engine.rootObjects()[0]
    
    
    #finding the stuff from the qml to use in python
    startsetzen = win.findChild(QObject, "Start setzen")
    textInputBreitengradStart = win.findChild(QObject, "textInputBreitengradStart")
    textInputLaengengradStart = win.findChild(QObject, "textInputLaengengradStart")
    mapcentercircle = win.findChild(QObject, "mapcentercircle")
    
    #work in progress
    #if start setzen is clicked take the coordinates entered into neuer Breitengrad and 
    #neuer Längengrad, delete the circle of the old start point and draw a circle at the new
    #starting point
    @pyqtSlot(QVariant)
    def startSetzen():
        print("Start setzen clicked")
        neuerBreitengradStart = textInputBreitengradStart.property("text")
        print(neuerBreitengradStart)
        neuerLaengengradStart = textInputLaengengradStart.property("text")
        print(neuerLaengengradStart)
        
        
    startsetzen.clicked.connect(startSetzen)
    
    
    win.showFullScreen()

    sys.exit(myApp.exec_())