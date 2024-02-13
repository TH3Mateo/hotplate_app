import threading as th
import connection_module as cm

import struct


class Heater:
    def __init__(self):
        self.device = cm.USB_device()
        self.device.start()

        self.target_temperture = 0
        self.actual_temperture = None
        self.actual_heater_state = None
        self.printer = None  # This is a function that will be called to print to the console
        self.start_sequence()
        self.device.connection.write([0x00] * self.device.setts["communication.buffSize"])

    def start_sequence(self):
        self.dispatcher = th.Thread(target=self.queue_dispatcher, daemon=True)
        self.dispatcher.start()

    def switch_builtin_led(self, state):
        try:
            self.device.set_led(1, state)
        except Exception as e:
            print("Could not change builtin LED state")
            print("Tried changing to ", state, "with result: ", str(e))

    def switch_external_led(self, state):
        try:
            self.device.set_led(2, state)
        except Exception as e:
            print("Could not change external LED state")
            print("Tried changing to ", state, "with result: ", str(e))

    def set_target_temperture(self):
        print("Setting target temperature to ", self.target_temperture)
        try:
            self.device.set_value("SET_TARGET_TEMPERATURE", int(self.target_temperture))
        except Exception as e:
            print("Could not change target temperature")
            print("Tried changing to ", self.target_temperture, "with result: ", str(e))

    def get_temperture(self):
        try:
            self.device.set_value("REQUEST_ACTUAL_TEMPERATURE")
            print(self.device.receive_queue.qsize())
        except Exception as e:
            print("Could not request temperature")
            print(str(e))

    def queue_dispatcher(self):
        print("Queue dispatcher started")
        while True:
            if not self.device.receive_queue.qsize() == 0:

                msg = self.device.receive_queue.get()
                print("msg: ", msg)
                match msg[0]:

                    case 0x01:
                        self.actual_temperture = struct.unpack('f', msg[-4:])
                        print("Actual temperature received: ", self.actual_temperture)
                        self.printer(str(self.actual_temperture))
                    case 0x02:
                        temp = struct.unpack('f', msg[-4:])
                        print("target temperature set: ", temp)
                        self.printer("target temp set: " + str(temp))
                    case 0x08:
                        print("LED state set")
                        self.printer(" ".join(msg[1:].decode("utf-8").split()))

                    case 0x05:
                        print("Heater state requested")
                        self.actual_heater_state = int.from_bytes(msg[1:], byteorder="big")

                    case _:
                        pass
