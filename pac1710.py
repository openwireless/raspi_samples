#! /usr/bin/env python3

# PAC1710(Curent sensor) Control library
#   2019.10.18 R1.0  A.Daikoku

import smbus
import time

_i2cAddr = 0x18     # default address when open

bus = smbus.SMBus(1)

def setup():
    pass        # nothing to do

def getID():
    data = bus.read_i2c_block_data(_i2cAddr, 0xfd, 2)
    return (data[0] << 8 | data[1])

def getCurrent():
    ch1Vsense = bus.read_i2c_block_data(_i2cAddr, 0x0d, 2)
    ch1Vsource = bus.read_i2c_block_data(_i2cAddr, 0x11, 2)
    ibus_mA = ((ch1Vsense[0] << 8 | (ch1Vsense[1])) >> 4) * 3.9082
    if (ibus_mA > 4000):
        ibus_mA = 0.0   # may be a noise
    return (ibus_mA)

if __name__ == '__main__':
    try:
        setup()
        id = getID()
        print('ID: %x' % id)
        while True:
            i = getCurrent()
            print('%.2f' % i)
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        exit(0)

