import smbus
import time

bus = smbus.SMBus(1)

def setup(Addr):

    global address
    address = Addr

def read(channel):
    try:

        if channel == 0:
            bus.write_byte(address, 0x40)
        if channel == 1:
            bus.write_byte(address, 0x41)
        if channel == 2:
            bus.write_byte(address, 0x42)
        if channel == 3:
            bus.write_byte(address, 0x43)

        bus.read_byte(address)# dummy read to start conversion
    except Exception as e:

        print ("Address: %s" % address)
        print (e)

    return bus.read_byte(address)



def write(value):
    try:
        temp = value #move string value to temp
        temp = int(temp) # change string to integer
        # print temp to see on terminal else comment out
        bus.write_byte_data(address, 0x40, temp)

    except Exception as e:
        print ("Error: Device address: 0x%2X" % address)
        print (e)

if __name__ == "__main__":

    setup(0x48)
    while True:
        print ("AIN0 = ", read(0))
        print ("AIN1 = ", read(1))
        print ("AIN2 = ", read(2))
        print ("AIN3 = ", read(3))
        print (" ")

        tmp = read(0)
        tmp = tmp * (255 - 125) / 255 + 125 # LED won't light up below 125, so convert '0-255' to '125-255'write(tmp)
        time.sleep(1.0)

        