#!/usr/bin/python3
#
#CTF_blah_somehting by shawsuraj
#
#Tools/Commands - nmap, dirb, wpscan, xterm, wget

from os import system
import sys
import multiprocessing
from Defs.actions import *


if __name__ == "__main__" :

    try :
        header()
        baseSetup()

        startScan()
        startAttack()
    except KeyboardInterrupt:
        endMessage()
        exit(0)
