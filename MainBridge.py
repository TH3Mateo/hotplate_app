import sys
import time
from pathlib import Path

from PySide6.QtCore import QObject, Slot, Property, Signal
from PySide6.QtQml import QQmlApplicationEngine, QmlElement, qmlRegisterType, QQmlComponent
import threading as th
import time as t

import connection_module as cm
from USB_cout import USB_console

QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class MainBridge(QObject):
    new_output_line = Signal()


    def __init__(self):
        super().__init__()
        self.device = cm.USB_device()
        self.usb_output = "efvesvsrvs"
        self.start_sequence()
        # t.sleep(2)
        # self.usb_output = "ąąą"

    def start_sequence(self):
        self.updater = th.Thread(target=self.output_printer, daemon=True)
        self.updater.start()

        th.Thread(target=self.queue_test, daemon=True).start()

    def queue_test(self):

        while True:
            t.sleep(1)
            self.device.receive_queue.put("test")

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

    def output_printer(self):
        self.received_list = []
        # print("output printer started")
        while True:
            # self.usb_output = "iiiii"
            # self.usb_output = "xd"

            if not self.device.receive_queue.empty():
                self.received_list.append(self.device.receive_queue.get())
                # print("\n".join(self.received_list))
                # self.new_output_line.emit()
                # self.usb_output = self.device.receive_queue.get()
                # print(self.received_list[-1])
                print(self.received_list[-1] if self.received_list else "empty")
                self.usb_output = "\n".join(self.received_list)

                if len(self.received_list) > 6:
                    self.received_list.pop(0)

            t.sleep(0.1)
