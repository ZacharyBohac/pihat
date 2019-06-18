#!/usr/bin/env python
from sense_hat import SenseHat 
sense = SenseHat()

#defines colours
Rasberry =(255, 0, 125)
Green = (0, 255, 0)

speed = 0.05

message = ("1660s sea shanties")

sense.show_message(message, speed, text_colour=Green, back_colour=Rasberry)

sense.clear()
#this writes a message in a color
