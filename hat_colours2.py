#!/usr/bin/env python
from sense_hat import SenseHat 
sense = SenseHat()
import time

red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)

sense.show_letter("U", red)
time.sleep(1)
sense.show_letter("S", green)
time.sleep(1)
sense.show_letter("A", blue)
time.sleep(1)
sense.clear()
