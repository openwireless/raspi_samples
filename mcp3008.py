#! /usr/bin/env python3

# ADC(MCP3008) Control library
#   2018.03.05 R1.0  A.Daikoku

import spidev

_spi = spidev.SpiDev()
_spi.open(0, 0)              # SPI Bus #0 and Use SS0
_spi.max_speed_hz = 3000000  # Set SPI Clock as 3MHz

def readAdcValue(ch):
    """Read the value of ch"""
    global _spi
    adc = _spi.xfer2([1, (8 + ch) << 4, 0])
    data = ((adc[1] & 7) << 8) + adc[2]
    return data

def convertVoltage(value):
    """Convert ADC value to voltage. Unit is [mV]"""
    volts = (value * 3300.0) / 1023.0
    volts = round(volts, 0)
    return int(volts)

def readVoltage(ch):
    """Read the voltage of ch. Unit is [mV]"""
    adcValue = readAdcValue(ch)
    mV = convertVoltage(adcValue)
    return int(mV)

# Test script 
if __name__ == '__main__':
    import sys
    import time
    if (len(sys.argv) == 1):
        ch = 0
    else:
        ch = int(sys.argv[1])

    try:
        while True:
            data = readAdcValue(ch)
            print("adc: {:4} ".format(data))
            mV = convertVoltage(data)
            print("mV:  {:4}".format(mV))
            time.sleep(0.2)

    except KeyboardInterrupt:
        _spi.close()
        sys.exit(0)

