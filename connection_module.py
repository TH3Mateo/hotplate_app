import serial.tools.list_ports
import serial



def start():
    portlist = []
    portinfo = serial.tools.list_ports.comports()
    for one in portinfo: print(str(one)); portlist.append(str(one)[:(str(one).find(" "))])
    connection = serial.Serial(baudrate=115200)

    if portlist:

        for i in range(len(portlist)):
            try:
                connection.port = portlist[i]
                connection.open()
            except:
                pass

    else:
        # exit()
        pass
    return connection

def filter_temp(string):
    if "rd " in string:
        return string[3:]


# def main():
#     filter_temp("rd 47")
#
#
#
#
# if __name__ == '__main__':
#     main()
