#!/usr/bin/env python3
from ev3dev2.motor import * 
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import *
from ev3dev2.sound import *
from legoFunctions import *
from commandFunction import *
import scanner

scancube()
print(scanner.cubestring)