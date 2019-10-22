#! /usr/bin/env python3

# MMA8452Q(Acceleration sensor) Control library
#   2019.10.18 R1.0  A.Daikoku

import smbus
import time

_i2cAddr = 0x1d
_scale = 0

bus = smbus.SMBus(1)

def getFIFOentries():
    return ((bus.read_byte_data(_i2cAddr, 0x00) & 0x3F) >> 1)

def setup(odr, range, i2cAddr = 0x1d):
    global _i2cAddr
    global _scale
    _i2cAddr = i2cAddr
    # REG1 <= ODR(100/200/400/800Hz) and Low-noise
    reg1 = 0x04
    if odr == 50:
        reg1 |= 0x20
    elif odr == 100: 
        reg1 |= 0x18 
    elif odr == 200: 
        reg1 |= 0x10 
    elif odr == 400: 
        reg1 |= 0x08 
    elif odr == 800: 
        reg1 |= 0x00        # default
    else:
        reg1 |= 0x18
    bus.write_byte_data(_i2cAddr, 0x2a, reg1)
    # XYZ_DATA_CFG <= range(2/4/8g)
    xyz_data_cfg = 0x00
    if range == 2:
        xyz_data_cfg |= 0x00
        _scale = 1024
    elif range == 4:
        xyz_data_cfg |= 0x01
        _scale = 512
    elif range == 8:
        xyz_data_cfg |= 0x02
        _scale = 256
    else:
        xyz_data_cfg |= 0x02    # default
        _scale = 1024
    bus.write_byte_data(_i2cAddr, 0x0e, xyz_data_cfg)
    # REG_F_SETUP <= F_MODE_FILL_BUF - Use FIFO
    bus.write_byte_data(_i2cAddr, 0x09, 0x80)
    # REG2 <= MODE_HIGH_RES
    bus.write_byte_data(_i2cAddr, 0x2b, 0x02)
    time.sleep(0.1)
    # Go!
    reg1 = bus.read_byte_data(_i2cAddr, 0x2a)
    reg1 |= 0x01
    bus.write_byte_data(_i2cAddr, 0x2a, reg1)

def read():
    global _scale
    # Wait until the data is ready
    while (getFIFOentries() < 6):
        pass
    # read xyz data and convert [g] unit
    data = bus.read_i2c_block_data(_i2cAddr, 0x01, 6)
    xAcc = (data[0] * 256 + (data[1] & 0xFC)) / 16
    if xAcc > 2047 :
        xAcc -= 4096
    yAcc = (data[2] * 256 + (data[3] & 0xFC)) / 16
    if yAcc > 2047 :
        yAcc -= 4096
    zAcc = (data[4] * 256 + (data[5] & 0xFC)) / 16
    if zAcc > 2047 :
        zAcc -= 4096
    return (xAcc/_scale, yAcc/_scale, zAcc/_scale)


if __name__ == '__main__':
    try:
        setup(100, 4)
        time.sleep(0.1)
        while True:
            xyz = read()
            print(xyz)
    except KeyboardInterrupt:
        pass
    finally:
        exit(0)
