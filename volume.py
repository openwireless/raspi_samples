# volume.py

import sys
import time
import mcp3008

CH = 0

try:
    while True:
        data = mcp3008.readAdcValue(CH) 
        print("adc: {:4} ".format(data))
        mV = mcp3008. convertVoltage(data)
        print("mV:  {:4}".format(mV))
        time.sleep(0.2)

except KeyboardInterrupt:
    sys.exit(0)

