import sys
import threading
import time
from pathlib import Path
import config
from PySide6.QtCore import QObject, Slot, Property, Signal
from PySide6.QtQml import QQmlApplicationEngine, QmlElement, qmlRegisterType, QQmlComponent
import threading as th
import time as t
from heater import Heater

QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1

offline_debug = config.Config("settings.cfg")["app.offline_debug"]
debug = config.Config("settings.cfg")["app.debug"]


@QmlElement
class MainBridge(QObject):
    new_output_line = Signal()
    current_temperature_updated = Signal()

    def __init__(self):
        super().__init__()
        if not offline_debug:
            self.heater = Heater()
            self.heater.printer = self.output_printer
            self.heater.send_actual_temp = self.temp_setter

        self.console_output = "  "
        self.current_temperature = " "

        print("MainBridge init")

        self.console_text_list = []

        def bait():
            time.sleep(2)
            self.current_temperature = "45"

        threading.Thread(target=bait).start()




        # th.Thread(target=self.queue_test, daemon=True).start()

    def console_output(self, val=None):
        if val is None:
            return self._console_output
        else:
            self._console_output = val
            self.new_output_line.emit()

    console_output = Property(str, fget=console_output, fset=console_output, notify=new_output_line)

    def current_temperature(self, val=None):
        if val is None:
            return self._current_temperature
        else:
            self._current_temperature = val
            self.current_temperature_updated.emit()

    current_temperature = Property(str, fget=current_temperature, fset=current_temperature,
                                   notify=current_temperature_updated)

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

    @Slot()
    def on_sampling_rate_change(self, value):
        self.heater.sampling_rate = value

    def output_printer(self, text):

        # print("output printer started")
        self.console_text_list.append(text)

        self.console_output = "\n".join(self.console_text_list)

        if len(self.console_text_list) > 6:
            self.console_text_list.pop(0)

    def temp_setter(self, value):
        self.current_temperature = value
