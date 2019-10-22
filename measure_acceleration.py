# measure_acceleration

import mma8452q as acc
import time

I2C_ADDR = 0x1d     # i2c address
ODR = 400           # Output Data Rate[Hz]
RANGE = 4           # Acceleration range [+/-g]

acc.setup(ODR, RANGE, I2C_ADDR)
time.sleep(0.1)

try:
    last = time.time()
    while True:
        xyz = acc.read()
        print("%.4f,%+1.3f,%+1.3f,%+1.3f" % (time.time(), xyz[0], xyz[1], xyz[2]))

except KeyboardInterrupt:
    pass
finally:
    pass
