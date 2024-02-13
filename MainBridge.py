import sys
import time
from pathlib import Path

from PySide6.QtCore import QObject, Slot, Property, Signal
from PySide6.QtQml import QQmlApplicationEngine, QmlElement, qmlRegisterType, QQmlComponent
import threading as th
import time as t
from heater import Heater

QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class MainBridge(QObject):
    new_output_line = Signal()


    def __init__(self):
        super().__init__()
        self.heater = Heater()
        self.heater.printer = self.output_printer

        self.console_output = "  "
        print("MainBridge init")

        self.console_text_list = []

    # def start_sequence(self):
    #     self.updater = th.Thread(target=self.output_printer, daemon=True)
    #     self.updater.start()

        # th.Thread(target=self.queue_test, daemon=True).start()

    def console_output(self, val=None):
        if val is None:
            return self._console_output
        else:
            self._console_output = val
            self.new_output_line.emit()

    console_output = Property(str, fget=console_output, fset=console_output, notify=new_output_line)

    @Slot(int)
    def on_BULTIN_LED_change(self, state):
        self.heater.switch_builtin_led(state)

    @Slot(int)
    def on_EXTERNAL_LED_change(self, state):
        self.heater.switch_external_led(state)

    @Slot(str)
    def set_target_temp_value(self, temp):
        self.heater.target_temperture = temp

    @Slot()
    def on_target_temp_set(self):
        self.heater.set_target_temperture()

    @Slot()
    def on_request_temp(self):
        self.heater.get_temperture()

    def output_printer(self, text):

        # print("output printer started")
        self.console_text_list.append(text)

        self.console_output = "\n".join(self.console_text_list)

        if len(self.console_text_list) > 6:
            self.console_text_list.pop(0)
