import sys
import time
from pathlib import Path

from PySide6.QtCore import QObject, Slot, Property, Signal
from PySide6.QtQml import QQmlApplicationEngine, QmlElement, qmlRegisterType, QQmlComponent
from PySide6.QtGui import QTextBlock, QTextFrame, QTextObject
import threading as th
import time as t

import connection_module as cm

QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


class USB_console(QTextObject):
    def __init__(self, input_device: cm.USB_device):
        super().__init__()
        self.device = input_device
        self.updater = th.Thread(target=self.output_printer)
