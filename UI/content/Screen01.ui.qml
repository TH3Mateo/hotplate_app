

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.5
import QtQuick.Controls 6.5

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height
    color: "#ee0c0c"

    Rectangle {
        id: rectangle1
        x: -312
        y: -396
        width: 681
        height: 792
        color: "#871616"
        z: 0
    }

    Button {
        id: button
        text: qsTr("Press me")
        anchors.verticalCenter: parent.verticalCenter
        checkable: true
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Text {
        id: label
        width: 170
        height: 72
        color: "#fcf7f7"
        text: qsTr("Hello UI")
        anchors.top: button.bottom
        font.pointSize: 17
        anchors.horizontalCenterOffset: -21
        font.family: Constants.font.family
        anchors.topMargin: 32
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
