#primary actions
import os
import sys
from time import sleep
import shutil
import socket
from core.scans import *
from core.attack import *

#Base Setup
def baseSetup() :
    global n, ip, verbose
    verbose = False
    n = nIP()
    ip = setIP()
    if os.path.isdir('Output') :
        shutil.rmtree("Output")
    # if os.path.isdir('Data') :
    #     shutil.rmtree("Data")
    os.makedirs("Output")
    # os.makedirs("Data")

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

def dir(*ip) :
    for i in range(n) :
        os.system('mkdir Output/{}'.format(ip[i]))
        # os.system('mkdir Data/{}'.format(ip[i]))

def execXterm(cmnd) :
    os.system('xterm -e bash -c "{}" &'.format(cmnd))

def execGnome_terminal(cmnd) :
    os.system('gnome-terminal -q -- /bin/sh -c "python3 {}"'.format(cmnd))

def header():
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


# def mainMenu():
#     os.system('clear')
#     print ('''
#
#  █████  █     █ ███████ █       ███████ ██████  █     █    █    ███████  █     █ ██████  ███████
# █     █ █     █ █     █ █       █       █     █ █     █   █ █      █     █     █ █     █ █
# █       █     █ █     █ █       █       █     █ █     █  █   █     █     █     █ █     █ █
# █       ███████ █     █ █       █████   ██████  ███████ █     █    █     █     █ ██████  █████
# █       █     █ █     █ █       █       █     █ █     █ ███████    █     █     █ █   █   █
# █     █ █     █ █     █ █       █       █     █ █     █ █     █    █     █     █ █    █  █
#  █████  █     █ ███████ ███████ ███████ ██████  █     █ █     █    █      █████  █     █ ███████
#
#
#                                                                                     BY:SHAWSURAJ
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')

def endMessage() :
    header()
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
" Finishing up...\n"''')
    sleep(1.25)

def startScan() :
    for i in range(n) :
        bScan(ip[i])

def bScan(ip) :
    # exec(firefox(ip))
    execXterm(nmapScan(ip))
    execXterm(dirbScan(ip))
    execXterm(wpScan(ip))
    execXterm(wget(ip))
    #execXterm(checkSqli(ip))


# def startAttack() :
#     for i in range(n) :
#         bAttack(ip[i])
#
# def bAttack(ip) :
#
#     services = list()
#     # services.append("ftp")
#     services.append("ssh")
#
#     for service in services :
#         try :
#             execGnome_terminal(service())
#         except Exception :
#             pass

    # for port in ssh.values() :
    #     if portScanner(ip, port) :
    #         execGnome_terminal(sshAttack(ip))
