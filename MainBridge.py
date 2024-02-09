import sys
import time
from pathlib import Path

from PySide6.QtCore import QObject, Slot, Property, Signal
from PySide6.QtQml import QQmlApplicationEngine, QmlElement, qmlRegisterType, QQmlComponent
import threading as th
import time as t

import connection_module as cm

QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class MainBridge(QObject):
    new_output_line = Signal()

    def __init__(self):
        super().__init__()
        self.device = cm.USB_device()
        self.usb_output = "efvesvsrvs"

    def usb_output(self, val=None):
        if val is None:
            return self._usb_output
        else:
            self._usb_output = val
            self.new_output_line.emit()

    usb_output = Property(str, fget=usb_output, fset=usb_output, notify=new_output_line)

    @Slot(int)
    def on_BULTIN_LED_change(self, state):
        try:
            self.device.set_led(0, state)
        except Exception as e:
            print("Could not change builtin LED state")
            print("Tried changing to ", state, "with result: ", str(e))

    @Slot(str)
    def set_target_temp_value(self, temp):
        self.target_temp = temp

    @Slot()
    def on_target_temp_set(self):
        print("Setting target temperature to ", self.target_temp)
        # try:
        #     self.device.set_value("SET_TARGET_TEMPERATURE", self.target_temp)
        # except Exception as e:
        #     print("Could not change target temperature")
        #     print("Tried changing to ", self.target_temp, "with result: ",str(e) )
