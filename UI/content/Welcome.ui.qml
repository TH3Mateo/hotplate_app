import QtQuick 6.5
import QtQuick.Controls 6.5

//import FirstBridge 1.0
Rectangle {
    id: rectangle
    width: 640
    height: 480
    color: "#ee0c0c"

    Text {
        id: label
        y: 146
        width: 84
        height: 39
        color: "#fcf7f7"
        text: qsTr("Hello UI")
        font.pointSize: 17
        anchors.horizontalCenterOffset: -16
        //        font.family: Constants.font.family
        anchors.topMargin: -84
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Item {
        id: item1
        x: 336
        y: 182
        width: 200
        height: 200
    }

    Text {
        id: text1
        x: 174
        y: 300
        width: 220
        height: 56
        text: qsTr("Loading screen czy cos")
        font.pixelSize: 18
    }
}
