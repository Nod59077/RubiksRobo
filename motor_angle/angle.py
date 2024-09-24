#!/usr/bin/env python3
from ev3dev2.motor import *
import time as t

m = MediumMotor(OUTPUT_A)

while True:
    angle = m.position
    print (angle)
    t.sleep(5)