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
        x: 10
        y: 10
        icon.color: "#1034b7"
        state: ""
        checkable: true
    }

    Text {
        id: label
        width: 84
        height: 39
        color: "#fcf7f7"
        text: qsTr("Hello UI")
        anchors.top: button.bottom
        font.pointSize: 17
        anchors.horizontalCenterOffset: -30
        font.family: Constants.font.family
        anchors.topMargin: 11
        anchors.horizontalCenter: parent.horizontalCenter
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
