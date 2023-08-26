import importlib.util as ilu

try:
    import connection_module as coms
except:
    spec1 = ilu.spec_from_file_location("coms",r"D:\PycharmProjects\heater_gui\connection_module.py")
    coms = ilu.module_from_spec(spec1)
    spec1.loader.exec_module(coms)


@coms.add_method
def set_value(self, parameter: str, value=None):
    packet = [self.setts["communication.buffSize"]]
    packet[0] = self.commands[parameter]

    self.transmit_queue.put()


@coms.add_method
def set_led(self, led_nr, value):
    packet = [self.setts["communication.buffSize"]]
    packet[0] = self.commands["SET_LED_STATE"]
    print("ergr")