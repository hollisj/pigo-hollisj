#from gopigo import

__author__ = 'justinhollis'
from gopigo import *
import time

class Pigo:

    isMoving = False
    servoPos = 90


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

bob = Pigo()
bob.fwd()
time.sleep(2)
bob.stop()



