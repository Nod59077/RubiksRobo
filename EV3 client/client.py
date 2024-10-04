#!/usr/bin/env python3
import requests                                 #import all necessary libraries
from legoFunctions import *
from commandFunction import command
import scanner
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import *

color_sensor = ColorSensor(INPUT_1)

def send_cube_state():
    color_sensor.MODE_RGB_RAW
    scancube()          #scan the cube
    cube_state = scanner.cubestring     #cube_state becomes a string of all coloured tiles on the cube
    url = 'http://192.168.137.1:5000/solve'
    response = requests.post(url, json={'cube_state': cube_state})     #send cube string to server
    
    if response.status_code == 200:
        solvelist = response.json().get('solution', [])     #solvelist = solution
        print('Solution received: ' + str(solvelist))
        for m in solvelist:         #perform moves in solvelist using command function
            command(m)
        lift()
        quit()
    else:
        print('Error')

if __name__ == '__main__':
    send_cube_state()