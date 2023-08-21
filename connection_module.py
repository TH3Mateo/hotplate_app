from serial.tools.list_ports_windows import comports
import serial
import config
import threading
import queue


class USB_device:
    def __init__(self) -> None:
        self.connection = None
        self.con_lock = threading.Lock()
        self.COMport = None
        self.setts = config.Config("settings.cfg")
        self.commands = config.Config("commands.cfg")
        self.transmit_queue = queue.Queue()
        self.receive_queue = queue.Queue()

    def find_device_port(self):
        portinfo = comports()
        if portinfo:

            for com, info, id in sorted(portinfo):
                if str(self.setts["device.vendor_id"]+":"+self.setts["device.product_id"]) in id:
                    return com

            print(Exception("no devices found"))
            exit(1)

    def start_connection(self, com):
        self.connection = serial.Serial(baudrate=115200)
        try:
            self.connection.port = com
            print("connected to port ", com)
            self.connection.open()
        except:
            del self.connection
            raise Exception("could not connect to port ", com)

    def _SendThreadloop(self):
        while True:
            if not self.transmit_queue.empty():
                command = self.transmit_queue.get()
                self.con_lock.acquire()
                self.connection.write(command)
                self.con_lock.release()
            else:
                pass

    def _ReceiveThreadloop(self):
        while True:
            with self.con_lock:
                self.receive_queue.put(self.connection.read(
                    size=self.setts["communication.buffSize"]))

    def set_value(self, command: str, value=None):
        packet = [self.setts["communication.buffSize"]]
        packet[0] = self.commands[command]

        self.transmit_queue.put()

    def set_led(self, led_nr, value):
        packet = [self.setts["communication.buffSize"]]
        packet[0] = self.commands["SET_LED_STATE"]

    def start(self):
        self.COMport = self.find_device_port()
        self.start_connection(self.COMport)

        TX = threading.Thread(target=self._SendThreadloop, args=())
        RX = threading.Thread(target=self._ReceiveThreadloop, args=())


# def list_vendors():
#     import usb.core

# # find USB devices
#     dev = usb.core.find(find_all=True)
#     # loop through devices, printing vendor and product ids in decimal and hex
#     for cfg in dev:
#         sys.stdout.write('Decimal VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct) + '\n')
#         sys.stdout.write('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')

#     #pyserial list comports
#     print("pyserial list comports output   ")
#     for port, desc, hwid in sorted(comports()):
#         print("{}: {} [{}]".format(port, desc, hwid))


# def main():
#     c = USB_device()
#     print(hex(c.commands["REQUEST_ACTUAL_TEMPERATURE"]))

# #
# #
# #
# if __name__ == '__main__':
#     main()
