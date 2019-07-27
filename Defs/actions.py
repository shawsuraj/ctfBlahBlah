#primary actions
import os
import sys
from time import sleep
import shutil
from Defs.scans import *

for arg in sys.argv :
    if arg == "-v" : #If true - show verbose
        verbose = True

#Base Setup
def baseSetup() :
    global n, ip, verbose
    verbose = False
    n = nIP()
    ip = setIP()
    if os.path.isdir('Output') :
        shutil.rmtree("Output")
    os.makedirs("Output")
    dir(*ip)
    sleep(2) #Just to wait

def nIP() :
    try :
        n = int(input("Number of IP's to scan : "))
        return n

    except ValueError :
        print('''      <--Enter INTEGER value only-->''')
        return nIP()

def setIP() :
    #Getting the ip's of the target machine
    ip = list()
    for i in range(n) :
        x = input("Enter the IP : ")
        ip.append(x)
    return ip

def startScan() :
    for i in range(n) :
        bScan(ip[i])


def dir(*ip) :
    for i in range(n) :
        os.system('mkdir Output/{}'.format(ip[i]))

def exec(cmnd) :
    os.system('xterm -e bash -c "{}" &'.format(cmnd))


def mainMenu():
    os.system('clear')
    print ('''

                     ██████     ████████████   ████████
                    ██     ██        ██        ██
                    ██               ██        ██
                    ██               ██        ██████
                    ██               ██        ██
                    ██     ██        ██        ██
                     ██████          ██        ██


                                                            BY:SHAWSURAJ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')

def endMessage() :
    mainMenu()
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-CHOLEBHATURE-CHOLEBHATURE-CHOLEBHATURE--CHOLEBHATURE-CHOLEBHATURE-CHOLEBHATURE-''')


def bScan(ip):
    exec(firefox(ip))
    exec(nmap_scan(ip))
    exec(dirb_scan(ip))
    exec(wp_scan(ip))
