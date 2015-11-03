#from gopigo import

__author__ = 'justinhollis'
from gopigo import *
import time

class Pigo:

    #####
    ##### BASIC STATUS AND METHODS
    #####


    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175,
              'rightspeed' 175}

    def __init__(self):
        print "I am alive and ready for war."

    def stop(selfself):
        self.isMoving = False
        while stop() != 1:
            time.sleep(.1)
            print "No brakes, save me"

    def fwd(selfself):
        self.isMoving = True
        while fwd() !=1:
            time.sleep(.1)
            print "I ate to much for breakfeast this morning."

    #####
    ##### COMPLEX METHODS
    #####

    #####
    ##### BASIC APP STARTS HERE
    #####

bob = Pigo()
bob.fwd()
time.sleep(2)
bob.stop()



