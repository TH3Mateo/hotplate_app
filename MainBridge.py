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
    current_heater_state_updated = Signal()

    def __init__(self):
        super().__init__()

        if not offline_debug:
            self.heater = Heater()
            self.heater.printer = self.output_printer
            self.heater.send_actual_temp = self.temp_setter
            self.heater.send_heater_state = self.heater_state_setter
            self.heater.send_actual_state_heater = self.heater_state_setter

        self._console_output = "  "
        self._current_temperature = " "
        self._current_heater_state = "0"

        print("MainBridge init")

        self.console_text_list = []

        def bait():
            time.sleep(2)
            self.temp_setter("45")
            self.heater_state_setter("69")

        threading.Thread(target=bait).start()

    # ----- Console output -----
    def console_output(self, val=None):
        if val is None:
            return self._console_output
        else:
            self._console_output = val
            self.new_output_line.emit()

    console_output = Property(str, fget=console_output, fset=console_output, notify=new_output_line)

    # ----- Current temperature -----
    def current_temperature(self, val=None):
        if val is None:
            return self._current_temperature
        else:
            self._current_temperature = val
            self.current_temperature_updated.emit()

    current_temperature = Property(str, fget=current_temperature, fset=current_temperature, notify=current_temperature_updated)

    # ----- Current heater state -----
    def current_heater_state(self, val=None):
        if val is None:
            return self._current_heater_state
        else:
            self._current_heater_state = val
            self.current_heater_state_updated.emit()

    current_heater_state = Property(str, fget=current_heater_state, fset=current_heater_state, notify=current_heater_state_updated)

    # ----- Slots -----
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

    # ----- Callbacks from Heater -----
    def output_printer(self, text):
        self.console_text_list.append(text)
        self.console_output = "\n".join(self.console_text_list[-6:]) 

    def temp_setter(self, value):
        self.current_temperature = value

    def heater_state_setter(self, value):
        self.current_heater_state = value