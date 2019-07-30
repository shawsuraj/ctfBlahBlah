import sys
from os import system
import socket

#Take input of wordlist and also set a default wotdlist.

def checkSSH(ip) :
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = sock.connect_ex((ip,22))
    sock.close()
    if res == 0:
       return True
    else :
       return False

def ssh_version(ip) :
    f = open("Data/{}/ssh_version.rc".format(ip), "w+")
    f.write("use auxiliary/scanner/ssh/ssh_version\n")
    f.write("set rhosts {}\n".format(ip))
    f.write("run\n")
    f.write("exit")
    f.close()

    system("msfconsole -q -r Data/{0}/ssh_version.rc -o Output/{0}/ssh_version.txt".format(ip))

def ssh_userEnum(ip) :
    f = open("ssh_userEnum.rc", "w+")
    f.write("use auxiliary/scanner/ssh/ssh_enumusers\n")
    f.write("set rhosts {}\n".format(ip))
    f.write("set user_file \n") #Set wordlist
    f.write("run\n")
    f.write("exit")
    f.close()

    system("msfconsole -q -r Data/{0}/ssh_userEnum.rc -o Output/{}/ssh_userEnum.txt".format(ip))

def ssh_login(ip) :
    f = open("ssh_login.rc", "w+")
    f.write("use scanner/ssh/ssh_login\n")
    f.write("set rhosts {}\n".format(ip))
    f.write("set blank_passwords true\n")
    f.write("set stop_on_success true\n")
    f.write("det pass_file \n") #Set wordlist
    f.write("set user_file \n") #Set wordlist
    f.write("run\n")
    f.write("exit")
    f.close

    system("msfconsole -q -r Data/{0}/ssh_login.rc -o Output/{}/ssh_login.txt".format(ip))

def sshMenu(ip) :

    print('''SSH servie is running on {0}

    1) SSH Version Check (METASPLOIT)
    2) SSH User Enumeration (METASPLOIT)
    3) SSH Login Brute-force (METASPLOIT)
    4) SSH Login Brute_force (HYDRA)
    '''.format(ip))

    option = int(input("Choose an option/options or enter 0 to exit : "))

    nOptions = [int(n) for n in str(option)]

    sshMain(ip)


def sshMain(ip) :
    # try :
    while True :
        for option in nOptions :
            if option == 1 :
                print("Scanning the version of SSH.")
                ssh_version(ip)

            elif option == 2 :
                print("Enumeratig")
                ssh_userEnum(ip)

            elif option == 3 :
                ssh_login(ip)

            elif option == 4 :
                system("hydra -L logins.txt -P pws.txt -M {} ssh".format(ip))

            elif option == 0 or option == '0' :
                return

            sshMenu()

    # except :
    #     sshMenu(ip)
try :
    ip = sys.argv[1]
    if checkSSH(ip) :
        sshMenu(ip)

except KeyboardInterrupt :
    print("Eat sleep rave repeat.")
