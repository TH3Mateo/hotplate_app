from serial.tools.list_ports_windows import comports
import serial
import config
import threading
import queue
import signal
import time
import sys
import dev_spec_layer

def add_method(func):
    setattr(USB_device, func.__name__, func)

class USB_device:
    def __init__(self) -> None:
        self.connection = None
        self.con_lock = threading.Lock()
        self.COMport = None
        self.setts = config.Config("settings.cfg")
        self.commands = config.Config("commands.cfg")
        self.transmit_queue = queue.Queue()
        self.receive_queue = queue.Queue()
        for method in dir(dev_spec_layer):
            if method.startswith("_"):
                continue
            else:
                if callable(getattr(dev_spec_layer, method)):
                    add_method(getattr(dev_spec_layer, method))


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
        self.connection.timeout = 0.1
        try:
            self.connection.port = com
            self.connection.open()
            print("connected to port ", com)

        except:
            del self.connection
            print("could not connect to port ", com)
            sys.exit()

    #######################################################################
    # PROBABLY BETTER TO JUST USE CONNECTION.WRITE INSTEAD OF THIS
    #######################################################################
    def _SendThreadloop(self):
        print("send thread started")
        while True:
            if not self.transmit_queue.empty():
                command = self.transmit_queue.get()
                print("command: ", command)
                self.con_lock.acquire()
                # print("sending")
                self.connection.write(bytearray(command))
                self.con_lock.release()
                # print("queue size: ", self.transmit_queue.qsize())
            else:
                pass

    def _ReceiveThreadloop(self):
        while True:
            rec = self.connection.read(size=self.setts["communication.buffSize"])
            if rec:
                self.receive_queue.put(rec)


    def start(self):
        self.COMport = self.find_device_port()
        self.start_connection(self.COMport)

        self._TX = threading.Thread(target=self._SendThreadloop, args=(), daemon=True)
        self._RX = threading.Thread(target=self._ReceiveThreadloop, args=(), daemon=True)
        self._TX.start()
        self._RX.start()
        signal.signal(signal.SIGINT, self.handler_setup())

    def handler_setup(self):
        thr  = (self._TX, self._RX)
        def handler(signum, frame):
            msg = "processes being killed..."
            print(msg, end="", flush=True)
            for t in thr:
                t.join()
            sys.exit()

        return handler

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




