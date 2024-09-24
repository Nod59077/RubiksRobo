#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import *
import time

color_sensor = ColorSensor(INPUT_1)
color_sensor.MODE_RGB_RAW
cubestring = ''

def scan():
    r, g, b = color_sensor.rgb
    global cubestring
    
    if 130<r<200 and 20<g<130 and 30<b<100:
        cubestring += 'r'
    elif 30<r<50 and 111<g<180 and 110<b<180:
        cubestring += 'g'
    elif 20<r<40 and 40<g<110 and 110<b<155:
        cubestring += 'b'
    elif 200<r<254 and 200<g<256 and 200<b<256:
        cubestring += 'o'
    elif r == 255 and 240<g<256 and b == 255:
        cubestring += 'w'
    else:
        cubestring += 'y'