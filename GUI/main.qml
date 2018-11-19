import QtQuick 2.0
import QtQuick.Window 2.2
import QtPositioning 5.1
import QtLocation 5.1
import QtQuick.Controls 1.0

Window
{
    visible: true
    width: 640
    height: 480
    color: "#666666"
    title: qsTr("StratosMapPy")
    visibility: Window.FullScreen

    Rectangle
    {
        id: menueLinks
        width: parent.width*0.25
        height: parent.height
        anchors.bottom: parent.bottom
        color: "#595959"
        Rectangle
        {
            id: startBereich
            width: parent.width
            height: parent.height*0.3
            //color:"#FF0000"
            border.color: "black"
            border.width: 3
            Text
            {
                id: textstartort
                text:"Startort"
                font.pixelSize:50
                anchors.horizontalCenter:parent.horizontalCenter
                anchors.top: parent.top
                anchors.topMargin: 2
            }
            Rectangle
            {
                id: rahmenBreitengradStart
                width: parent.width
                height: parent.height*0.3
                anchors.top: textstartort.bottom
                //color:"#FF0000"
                border.color: "black"
                border.width: 3
                Text
                {
                    id: textBreitengradStart
                    text:"Breitengrad"
                    font.pixelSize:25
                    anchors.top: rahmenBreitengradStart.top
                    anchors.topMargin: 10
                    anchors.horizontalCenter:parent.horizontalCenter
                }
                Rectangle
                {
                    id: rahmenBreitengradStartInput
                    width: parent.width
                    height: parent.height*0.4
                    border.color: "black"
                    border.width: 3
                    //color: "#FF5650"
                    anchors.top: textBreitengradStart.bottom
                    Text
                    {
                        id: textBreitengradStartInput
                        anchors.top: rahmenBreitengradStartInput.top
                        anchors.topMargin: 10
                        anchors.left: parent.left
                        anchors.leftMargin: 6
                        text: qsTr("Bitte Breitengrad des geänderten Startortes eingeben:")
                        font.pixelSize: 15
                    }

                    TextInput
                    {
                        id: textInputBreitengradStart
                        objectName: "textInputBreitengradStart"
                        anchors.top: rahmenBreitengradStartInput.top
                        anchors.topMargin: 10
                        anchors.left: textBreitengradStartInput.right
                        anchors.leftMargin: 6
                        text: qsTr("EINGABE")
                        font.pixelSize: 15
                    }
                }
            }
            Rectangle
            {
                id: rahmenLaengengradStart
                width: parent.width
                height: parent.height*0.3
                anchors.top: rahmenBreitengradStart.bottom
                anchors.topMargin: -3
                //color:"#FF0000"
                border.color: "black"
                border.width: 3
                Text
                {
                    id: textLaengengradStart
                    text:"Längengrad"
                    font.pixelSize:25
                    anchors.top: rahmenLaengengradStart.top
                    anchors.topMargin: 10
                    anchors.horizontalCenter: parent.horizontalCenter
                }
                Rectangle
                {
                    id: rahmenLaengengradStartInput
                    width: parent.width
                    height: parent.height*0.4
                    border.color: "black"
                    border.width: 3
                    //color: "#FF5650"
                    anchors.top: textLaengengradStart.bottom
                    Text
                    {
                        id: textLaengengradStartInput
                        anchors.top: rahmenLaengengradStartInput.top
                        anchors.topMargin: 10
                        anchors.left: parent.left
                        anchors.leftMargin: 6
                        text: qsTr("Bitte Längengrad des geänderten Startortes eingeben:")
                        font.pixelSize: 15
                    }
                    TextInput
                    {
                        id: textInputLaengengradStart
                        objectName: "textInputLaengengradStart"
                        anchors.top: rahmenLaengengradStartInput.top
                        anchors.topMargin: 10
                        anchors.left: textLaengengradStartInput.right
                        anchors.leftMargin: 6
                        text: qsTr("EINGABE")
                        font.pixelSize: 15
                    }
                }
            }
            Button
            {
                id: buttonStartsetzen
                objectName: "Start setzen"
                text: "Start setzen"
                anchors.left: parent.left
                anchors.leftMargin: 7
                anchors.top: rahmenLaengengradStart.bottom
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 3
            }
            ComboBox
            {
                id: comboBoxVorauswahlStartort
                anchors.right: parent.right
                anchors.rightMargin: 7
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 5
                editable: true
                model: [ "HTW Campus Altsaarbrücken", "HIZ", "Schloss" ]
            }


        }
        Rectangle
        {
            id: zielBereich
            width: parent.width
            height: parent.height*0.3
            anchors.top: startBereich.bottom
            //color:"#0174DF"
            border.color: "black"
            border.width: 3
            Text
            {
                id: textzielort
                text:"Zielort"
                font.pixelSize:50
                anchors.horizontalCenter:parent.horizontalCenter
                anchors.top: parent.top
                anchors.topMargin: 2
            }
            Rectangle
            {
                id: rahmenBreitengradZiel
                width: parent.width
                height: parent.height*0.3
                anchors.top: textzielort.bottom
                //color:"#FF0000"
                border.color: "black"
                border.width: 3
                Text
                {
                    id: textBreitengradZiel
                    text:"Breitengrad"
                    font.pixelSize:25
                    anchors.top: rahmenBreitengradZiel.top
                    anchors.topMargin: 10
                    anchors.horizontalCenter:parent.horizontalCenter
                }
                Rectangle
                {
                    id: rahmenBreitengradZielInput
                    width: parent.width
                    height: parent.height*0.4
                    border.color: "black"
                    border.width: 3
                    //color: "#FF5650"
                    anchors.top: textBreitengradZiel.bottom
                    Text
                    {
                        id: textBreitengradZielInput
                        anchors.top: rahmenBreitengradZielInput.top
                        anchors.topMargin: 10
                        anchors.left: parent.left
                        anchors.leftMargin: 6
                        text: qsTr("Bitte Breitengrad des Zielortes eingeben:")
                        font.pixelSize: 15
                    }

                    TextInput
                    {
                        id: textInputBreitengradZiel
                        anchors.top: rahmenBreitengradZielInput.top
                        anchors.topMargin: 10
                        anchors.left: textBreitengradZielInput.right
                        anchors.leftMargin: 6
                        text: qsTr("EINGABE")
                        font.pixelSize: 15
                    }
                }
            }
            Rectangle
            {
                id: rahmenLaengengradZiel
                width: parent.width
                height: parent.height*0.3
                anchors.top: rahmenBreitengradZiel.bottom
                anchors.topMargin: -3
                //color:"#FF0000"
                border.color: "black"
                border.width: 3
                Text
                {
                    id: textLaengengradZiel
                    text:"Längengrad"
                    font.pixelSize: 25
                    anchors.top: rahmenLaengengradZiel.top
                    anchors.topMargin: 10
                    anchors.horizontalCenter: parent.horizontalCenter
                }
                Rectangle
                {
                    id: rahmenLaengengradZielInput
                    width: parent.width
                    height: parent.height*0.4
                    border.color: "black"
                    border.width: 3
                    //color: "#FF5650"
                    anchors.top: textLaengengradZiel.bottom
                    Text
                    {
                        id: textLaengengradZielInput
                        anchors.top: rahmenLaengengradZielInput.top
                        anchors.topMargin: 10
                        anchors.left: parent.left
                        anchors.leftMargin: 6
                        text: qsTr("Bitte Längengrad des Zielortes eingeben:")
                        font.pixelSize: 15
                    }
                    TextInput
                    {
                        id: textInputLaengengradZiel
                        anchors.top: rahmenLaengengradZielInput.top
                        anchors.topMargin: 10
                        anchors.left: textLaengengradZielInput.right
                        anchors.leftMargin: 6
                        text: qsTr("EINGABE")
                        font.pixelSize: 15
                    }
                }
            }
            Button
            {
                id: buttonZielsetzen
                text: "Ziel setzen"
                anchors.left: parent.left
                anchors.leftMargin: 7
                anchors.top: rahmenLaengengradZiel.bottom
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 3
            }

        }
        Rectangle
        {
            id: sonstigesBereich
            width: parent.width
            height: parent.height*0.3
            anchors.top: zielBereich.bottom
            //color:"#FE2EF7"
            border.color: "black"
            border.width: 3
            Text
            {
                text:"Sonstiges"
                font.pixelSize:15
                anchors.horizontalCenter:parent.horizontalCenter
                anchors.top: parent.top
                anchors.topMargin: 2
            }
        }
        Rectangle
        {
            id: endeBereich
            width: parent.width
            height: parent.height*0.1
            anchors.top: sonstigesBereich.bottom
            //color:"#00FF00"
            border.color: "black"
            border.width: 3
            Text
            {
                text:"Ende"
                font.pixelSize:15
                anchors.horizontalCenter:parent.horizontalCenter
                anchors.top: parent.top
                anchors.topMargin: 2
            }

            Button {
                id: button
                x: 40
                y: 20
                text: qsTr("Ende")
                onClicked: Qt.quit();
            }
        }
    }

    Plugin
    {
        id: mapPlugin
        name: "osm"
    }

    //adds a map that is fully functional at the right side of the screen;
    //supports zooming, moving, drawing on the map
    Map
    {
        anchors.left:menueLinks.right
        width: parent.width*0.75
        height: parent.height
        plugin: mapPlugin
        center: QtPositioning.coordinate(49.235379, 6.975727)
        zoomLevel: 14

        //draws a circle around/at the htw saar campus alt-saarbrücken
        MapCircle
        {
            id: center
            objectName: "mapcentercircle"
            center
            {
                latitude: 49.235379
                longitude: 6.975727
            }
            radius: 20.0
            color: 'red'
            border.width: 3

        }
    }
}

