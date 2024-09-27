from ev3dev2.motor import *                  #import lego modules
import scanner
import time as t
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import *

color_sensor = ColorSensor(INPUT_1)
table = MediumMotor(OUTPUT_A)               #turntable on port a
flipper = LargeMotor(OUTPUT_B)              #flipper on port b
scanmover = LargeMotor(OUTPUT_C)            #motor moving scanner on port c

flipperstate = ''

def lift():                         #lift flipper
    global flipperstate
    flipper.on_for_degrees(20, 90)
    flipperstate = 'up'  
def lower():                        #lower flipper
    global flipperstate
    flipper.on_for_degrees(25, -90) 
    flipperstate = 'down' 
def turnS(factor):                  #turn side clockwise
    for i in range(factor):
        table.on_for_degrees(15, 90)
    t.sleep(0.1)    
def turnSprime(factor):             #turn side counter-clockwise
    for i in range(factor):
        table.on_for_degrees(15, -90)
    t.sleep(0.1)
def turnZ(factor):                  #flip cube
    for i in range(factor):
        flipper.on_for_degrees(20, -137)
        t.sleep(0.1)
        flipper.on_for_degrees(45, 137)
        t.sleep(0.1)     
def turnY(factor):                  #rotate entire cube clockwise
    lift()
    turnS(factor) 
    lower()
def turnYprime(factor):             #rotate entire cube counter-clockwise
    lift()
    turnSprime(factor)
    lower()

def turncube(degrees):
    table.on_for_degrees(15, degrees)
    t.sleep(0.3)
def movescanner(direction):
    scanmover.on_for_degrees(5, 25*direction)     #moves scanner over centre of cube (1 -> fd, -1 -> bk)
    t.sleep(0.3)

def yellowxblue():          #order of scanning faces "yellow" -> blue -> red -> green -> orange -> white
    turncube(-90)
    lower()
    turnZ(1)
    lift()
def standardturn():
    turncube(90)
    lower()
    turnZ(1)
    lift()
    turncube(-90)
def orangexwhite():
    lower()
    turnZ(1)
    lift()
    turncube(180)
def finishscan():       #ready cube for solver
    lower()
    turnZ(2)
    turnY(2)
    

def scanface():                         #scans the each face in a particular order, see server.py
    color_sensor.MODE_RGB_RAW
    t.sleep(1)
    if flipperstate == 'down':          #makes sure flipper is not down when face is scanned
        lift()
    scanmover.on_for_degrees(10, -84)
    turncube(-135)
    scanmover.on_for_degrees(5, -15)
    scanner.scan()
    scanmover.on_for_degrees(5, 15)
    turncube(-45)
    scanner.scan()
    turncube(-45)
    scanmover.on_for_degrees(5, -15)
    scanner.scan()
    scanmover.on_for_degrees(5, 15)
    turncube(135)
    scanner.scan()
    movescanner(1)
    scanner.scan()
    movescanner(-1)
    turncube(180)
    scanner.scan()
    turncube(-135)
    scanmover.on_for_degrees(5, -15)
    scanner.scan()
    scanmover.on_for_degrees(5, 15)
    turncube(45)
    scanner.scan()
    turncube(45)
    scanmover.on_for_degrees(5, -15)
    scanner.scan()
    scanmover.on_for_degrees(5, 15)
    turncube(-45)
    scanmover.on_for_degrees(10, 84)

def scancube():
    scanface()      #scan "yellow"
    yellowxblue()
    scanface()      #scan blue
    standardturn()
    scanface()      #scan red
    standardturn()
    scanface()      #scan green
    standardturn()
    scanface()      #scan orange
    orangexwhite()
    scanface()      #scan white
    finishscan()    #default orientation