#!/usr/bin/env python
# this script will display letters with random colors on the Pi Hat
from sense_hat import SenseHat 
sense = SenseHat()
import random
import time
#assign a random integer between 0 and 255 to a variable named r
r = random.randint(0,255)

sense.show_letter("U", (r, 0, 0))
time.sleep(1)
sense.show_letter("S", (0, r, 0))
time.sleep(1)
sense.show_letter("A", (0, 0, r))
time.sleep(1)

sense.clear()

