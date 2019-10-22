# measure_current.py

import time
import pac1710

PERIOD = 0.01   # Measurement cycle[Sec.]

try:
    pac1710.setup()
    last = 0
    while True:
        if (time.time() - last >= PERIOD):
            last = time.time()
            i = pac1710.getCurrent()
            print('%.3f,%.2f' % (time.time(), i))

except KeyboardInterrupt:
    pass

finally:
    pass
