#!/usr/bin/env python3
from legoFunctions import *     #import broken down moves

def command(command):
    moves = {"F":  ['Z', 'Sprime', 'Z3']        #moves is a dictionary breaking down each move
            ,"F2": ['Z', 'S2', 'Z3']  
            ,"F'": ['Z', 'S', 'Z3']
            ,"B":  ['Z3', 'Sprime', 'Z']
            ,"B2": ['Z3', 'S2', 'Z']
            ,"B'": ['Z3', 'S', 'Z']
            ,"U":  ['Z2', 'Sprime', 'Z2']  
            ,"U2": ['Z2', 'S2', 'Z2']
            ,"U'": ['Z2', 'S', 'Z2']
            ,"D":  ['Sprime']
            ,"D2": ['S2']
            ,"D'": ['S']
            ,"L":  ['Yprime', 'Z', 'Sprime', 'Z3', 'Y']
            ,"L2": ['Yprime', 'Z', 'S2', 'Z3', 'Y']
            ,"L'": ['Yprime', 'Z', 'S', 'Z3', 'Y']
            ,"R":  ['Y', 'Z', 'Sprime', 'Z3', 'Yprime']
            ,"R2": ['Y', 'Z', 'S2', 'Z3', 'Yprime']
            ,"R'": ['Y', 'Z', 'S', 'Z3', 'Yprime']
            }

    movelist = moves[command]       #movelist becomes the actions associated with the move when it is called in command

    for move in movelist:           #each action that can be in movelist corresponds to an action of the robot
        if move == 'S':
            turnS(1)
        elif move == 'S2':
            turnS(2)
        elif move == 'Sprime':
            turnSprime(1)
        elif move == 'Y':
            turnY(1)
        elif move == 'Y2':
            turnY(2)
        elif move == 'Yprime':
            turnYprime(1)
        elif move == 'Z':
            turnZ(1)
        elif move == 'Z2':
            turnZ(2)
        elif move == 'Z3':
            turnZ(3)