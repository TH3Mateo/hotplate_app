import importlib.util as ilu
import config
try:
    import connection_module as coms
except:
    spec1 = ilu.spec_from_file_location("coms",r"D:\PycharmProjects\heater_gui\connection_module.py")
    coms = ilu.module_from_spec(spec1)
    spec1.loader.exec_module(coms)


# @coms.add_method
def set_value(self, parameter: str, value=None):
    packet = [0x00] * self.setts["communication.buffSize"]
    packet[0] = self.commands[parameter]
    if value:
        value = [item for item in (value).to_bytes(4, byteorder="big")]
        packet[-len(value):] = value
    # print(packet)
    self.connection.write(packet)


# @coms.add_method
def set_led(self, led_nr, value):
    # print(value)
    # print(self.setts["communication.buffSize"])
    packet = [0x00] * self.setts["communication.buffSize"]
    packet[0] = self.commands["SET_LED_STATE"]
    packet[-2] = led_nr
    packet[-1] = value
    # print(packet)
    self.connection.write(packet)
    # print("ergr")
