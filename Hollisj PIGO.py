#from gopigo import

__author__ = 'justinhollis'
from gopigo import *
import time

class Pigo:

    #####
    ##### BASIC STATUS AND METHODS
    #####

    STOP_DIST = 100
    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175,
              'rightspeed' 175, "dist": 100}

    def __init__(self):
        print "I am alive and ready for war."
        self.status['dist'] = us_dist(15)
    def stop(self):
        self.status["ismoving"] = False
        print "lets get going!!!"
            for x in range(6):
                stop()


    def fwd(self):
        self.status = True
        print "lets get going"
        for x in range(3):
            stop()

    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            return False
        else:
            return True

    def checkDist(self):
        self.status['dist'] = us_dist(15)
        print 'I see something in the distance' + str(self.status['dist']) + "mm away."
    #####
    ##### COMPLEX METHODS
    #####

    def dance(self):
        print "The music is in my soul, the beat wont let me stop"
        self.spin()
        self.shuffle()
        self.shakeServo()
        self.rturn()
        self.lturn()
        self.blink()

    #####
    ##### BASIC APP STARTS HERE
    #####
bob = Pigo()

while bob.keepGoing():
    bob.checkDist()
    bob.fwd()
    if !bob.keepGoing() == False
        break
    time.sleep(2)
    bob.stop()

bob.stop()

