import config
from PySide6.QtCore import (Qt, QEvent, QObject, Signal, Slot)
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QGuiApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtQml import qmlRegisterType, QQmlApplicationEngine

import sys

from mainview import MainWindow



if __name__ == "__main__":
    qmlRegisterType(MainWindow, "Main", 1, 0, "main.qml")

    app = QGuiApplication(sys.argv)
    engine  = QQmlApplicationEngine()

    main_window = MainWindow()
    engine.rootContext().setContextProperty("main_window", main_window)
    engine.load("Screen01.ui.qml")
    main_window.show()
    app.exec()
    
    
