import QtQuick 6.5
import WindowBridge 1.0


Window {
    id: mainwindow
    width: mainScreen.width
    height: mainScreen.height
    visible: true

    //    state = adapter.view

    //    visible: true
    //    title: "UI"

    WindowBridge {
        id: adapter
    }
    Welcome {
        id: mainScreen
        visible: adapter.xd === "first"
    }
    Main {
        id: secondScreen
        visible: adapter.xd === "second"
    }


    //    states: State {
    //        name: "hidden"
    //        PropertyChanges { target: myRect; opacity: 0 }
    //    }
    //    states:[
    //        State{
    //            name: "main"
    ////            when: adapter.view==1
    //            PropertyChanges{
    //                target: mainScreen
    ////                visible: true
    //            }
    //            PropertyChanges{
    //                target: secondScreen
    ////                visible: false
    //            }
    //        },
    //        State{
    //            name: "second"
    ////            when: adapter.view==2
    //            PropertyChanges{
    //                target: mainScreen
    ////                visible: false
    //            }
    //            PropertyChanges{
    //                target: secondScreen
    ////                visible: true
    //            }
    //        }
    //    ]
    //    state: "main"

}

