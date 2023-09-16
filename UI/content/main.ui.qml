import QtQuick 6.5
import QtQuick.Controls 6.5

Rectangle {
    id: rectangle
    width: 640
    height: 480
    color: "#ee0c0c"

    Button {
        id: button
        text: qsTr("Press me")
        //        anchors.verticalCenter: parent.verticalCenter
        //        anchors.verticalCenterOffset: 68
        //        anchors.horizontalCenterOffset: -100
        //        anchors.horizontalCenter: parent.horizontalCenter
        x: 144
        y: 164
        icon.color: "#6c7493"
        state: ""
        checkable: true
    }

    Text {
        id: label
        height: 39
        visible: true
        color: "#fcf7f7"
        text: qsTr("Hello UI")
        anchors.top: button.bottom
        verticalAlignment: Text.AlignVCenter
        font.pointSize: 17
        anchors.horizontalCenterOffset: -44
        font.family: Constants.font.family
        anchors.topMargin: 12
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Rectangle {
        id: rectangle1
        x: 305
        y: 140
        width: 200
        height: 200
        color: "#c8ce24"
    }

    states: [
        State {
            name: "clicked"
            when: button.checked

            PropertyChanges {
                target: label
                text: qsTr("Button Checked")
            }
        }
    ]
}
