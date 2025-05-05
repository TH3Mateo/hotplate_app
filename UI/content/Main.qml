import QtQuick 6.5
import QtQuick.Controls 6.5
import QtCharts
import MainBridge 1.0


Rectangle {
    id: rectangle
    width: 640
    height: 480
    color: "#132630"

    MainBridge {
        id: connector


    }
    Rectangle {
        id: rectangle1
        x: 29
        y: 295
        width: 245
        height: 155
        color: "#00e27171"
        border.color: "#6e3232"
        border.width: 5
    }

    Text {
        id: text2
        x: 29
        y: 258
        width: 203
        height: 31
        color: "#aeb5b8"
        text: qsTr("USB READOUT")
        font.pixelSize: 24
    }

    Text {
        id: usb_output_textbox
        x: 39
        y: 301
        width: 226
        height: 143
        opacity: 1
        color: "#f49d9d"
        text: connector.console_output
        font.pixelSize: 15
        rightPadding: 3
        leftPadding: 3
        bottomPadding: 3
        topPadding: 3
    }

    Switch {
            signal
        aaaa
        id: builtin_led_sw
        x: 44
        y: 20
        text: qsTr("BUILTIN_LED")
        onCheckedChanged: {
            connector.on_BULTIN_LED_change(position)
        }
    }

    Switch {
        id: ext_led_sw
        x: 44
        y: 59
        text: qsTr("EXT_LED")
        onCheckedChanged: {
            connector.on_EXTERNAL_LED_change(position)
        }
    }

    Rectangle {
        id: rectangle2
        x: 29
        y: 205
        width: 146
        height: 43
        color: "#00150a14"
        border.color: "#6e3232"
        border.width: 4
    }

    Button {
        id: request_temp_btn
        x: 381
        y: 142
        text: qsTr("Request temperature")
        onPressed: {
            connector.on_request_temp()
        }
    }


    TextInput {
        id: target_temp_inp
        x: 37
        y: 209
        width: 116
        height: 43
        color: "#6e3232"

        font.pixelSize: 22
        selectByMouse: true
        activeFocusOnPress: true
        onEditingFinished: {
            connector.set_target_temp_value(text)
        }
    }

    Button {
        id: set_temp_btn
        x: 181
        y: 211
        text: qsTr("SET")

        onPressed: {
            connector.on_target_temp_set()
        }
    }

    ComboBox {
        id: comboBox
        x: 44
        y: 109
        width: 221
        height: 32
        displayText: "Temperature sampling rate"
        textRole: "Temperature sampling rate"
        model: ListModel {
            id: model
            ListElement {
                text: "Banana"
            }
            ListElement {
                text: "Apple"
            }
            ListElement {
                text: "Coconut"
            }
        }
        onAccepted: {
            if (find(editText) === -1)
                model.append({text: editText})
        }
    }

    Text {
        id: current_temp
        x: 399
        y: 59
        width: 164
        height: 62
        color: "#ab7679"
        text: connector.current_temperature
        font.pixelSize: 48
        topPadding: 0
    }

    Rectangle {
        id: rectangle3
        x: 381
        y: 40
        width: 200
        height: 101
        color: "#00ffffff"
        border.color: "#6e3232"
        border.width: 7
    }

    Text {
        id: text3
        x: 381
        y: 14
        width: 203
        height: 31
        color: "#aeb5b8"
        text: qsTr("CURRENT TEMPERATURE")
        font.pixelSize: 18
    }

    Text {
        id: text4
        x: 29
        y: 168
        width: 203
        height: 31
        color: "#aeb5b8"
        text: qsTr("TARGET TEMPERATURE")
        font.pixelSize: 18
    }

    // ChartView {
    //     id: line
    //     x: 320
    //     y: 22
    //     width: 300
    //     height: 300
    // backgroundColor: "#425159"
    // dropShadowEnabled: true
    // titleColor: "#ffffff"
    // LineSeries {
    //     name: "LineSeries"
    //     bestFitLineColor: "#ffffff"
    //     XYPoint { x: 1.1; y: 2.1 }


    // XYPoint {
    //     id: a
    //     x: 1
    //     y: 1.2
    // }
    //
    // XYPoint {
    //     id: b
    //     x: 2
    //     y: 3.3
    // }
    //
    // XYPoint {
    //     x: 5
    //     y: 2.1
    // }
    // }
    // }

    states: [
        State {
            name: "clicked"
            when: request_temp_btn.checked
        }
    ]
}
