#!/usr/bin/python3
#
#CTF_blah_somehting by shawsuraj
#
#Open Source

from os import system
import sys
import multiprocessing
from Defs.actions import *


if __name__ == "__main__" :

    try :
        mainMenu()
        baseSetup()
        
        startScan()

    except KeyboardInterrupt:
        endMessage()
        exit(0)
