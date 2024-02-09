import os
import sys
from pathlib import Path
import PySide6.QtCore as QtCore
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtQuickControls2 import QQuickStyle
from WindowBridge import WindowBridge
from MainBridge import MainBridge
from USB_cout import USB_console


# from FirstBridge import FirstScreenBridge

def qt_message_handler(mode, context, message):
    if mode == QtCore.qDebug:
        mode = 'Info'
    elif mode == QtCore.qWarning:
        mode = 'Warning'
    elif mode == QtCore.qCritical:
        mode = 'critical'
    elif mode == QtCore.qFatal:
        mode = 'fatal'
    else:
        mode = 'Debug'
    print("%s: %s (%s:%d, %s)" % (mode, message, context.file, context.line, context.file))



if __name__ == '__main__':

    QtCore.qInstallMessageHandler(qt_message_handler)
    app = QGuiApplication(sys.argv)
    QQuickStyle.setStyle("Material")
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).parent / "UI" / "content" / "App.qml"
    bridge0 = WindowBridge()

    qmlRegisterType(WindowBridge, "WindowBridge", 1, 0, "WindowBridge")
    qmlRegisterType(MainBridge, "MainBridge", 1, 0, "MainBridge")
    # qmlRegisterType(USB_console, "USB_console", 1, 0, "USB_console")

    # qmlRegisterType(MainBridge, "MainBridge", 1, 0, "MainBridge")
    # qmlRegisterType(FirstScreenBridge, "FirstBridge", 1, 0, "FirstScreenBridge")

    engine.load(qml_file)

    if not engine.rootObjects():

        sys.exit(-1)

    sys.exit(app.exec())
