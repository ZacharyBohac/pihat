#!/usr/bin/env python
# this script will display colors for individual pixels on the Pi Hat
from sense_hat import SenseHat
sense = SenseHat()
import random
import time
r = random.randint(0,255)
x = random.randint(1,7)
y = random.randint(1,7)

sense.set_pixel(x, y, (r, 0, r))

time.sleep(2)
sense.clear()
