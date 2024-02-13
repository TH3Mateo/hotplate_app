import QtQuick 6.5
import QtQuick.Controls 6.5
import MainBridge 1.0
import QtCharts

Rectangle {
    id: rectangle
    width: 640
    height: 480
    color: "#132630"

    MainBridge {
        id: connector
        console_output: {
            usb_output_textbox.text = console_output
        }
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
        color: "#6e3232"
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
        text: qsTr("Text")
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
        x: 123
        y: 29
        text: qsTr("BUILTIN_LED")
        onCheckedChanged: {
            connector.on_BULTIN_LED_change(position)
        }
    }

    Switch {
        id: ext_led_sw
        x: 123
        y: 75
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
        x: 123
        y: 124
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
        x: 210
        y: 209
        text: qsTr("SET")

        onPressed: {
            connector.on_target_temp_set()
        }
    }


    //    ChartView {
    //        id: spline
    //        x: 315
    //        y: 81
    //        width: 300
    //        height: 300
    //        SplineSeries {
    //            name: "LineSeries"
    //            XYPoint {
    //                x: 0
    //                y: 1
    //            }

    //            XYPoint {
    //                x: 3
    //                y: 4.3
    //            }

    //            XYPoint {
    //                x: 5
    //                y: 3.1
    //            }

    //            XYPoint {
    //                x: 8
    //                y: 5.8
    //            }
    //        }
    //    }

    states: [
        State {
            name: "clicked"
            when: request_temp_btn.checked
        }
    ]
}
