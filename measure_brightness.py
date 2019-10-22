# measure_brightness.py 

import sys
import time
import mcp3008

CH = 2

try:
    while True:
        data = mcp3008.readAdcValue(CH)
        print("adc: {:4} ".format(data))
        time.sleep(0.2)

except KeyboardInterrupt:
    sys.exit(0)

