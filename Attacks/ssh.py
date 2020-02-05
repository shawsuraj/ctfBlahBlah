import sys
from os import system
from time import sleep
import socket

#Take input of wordlist and also set a default wotdlist.

def ssh_version(ip, port) :
    f = open("Data/{}/ssh_version.rc".format(ip), "w+")
    f.write("use auxiliary/scanner/ssh/ssh_version\n")
    f.write("set rhosts {}\n".format(ip))
    f.write("set port {\n".format(port))
    f.write("run\n")
    f.write("exit")
    f.close()

    system("msfconsole -q -r Data/{0}/ssh_version.rc -o Output/{0}/ssh_version.txt".format(ip))

def ssh_userEnum(ip, port) :
    f = open("ssh_userEnum.rc", "w+")
    f.write("use auxiliary/scanner/ssh/ssh_enumusers\n")
    f.write("set rhosts {}\n".format(ip))
    f.write("set port {\n".format(port))
    f.write("set user_file \n") #Set wordlist
    f.write("run\n")
    f.write("exit")
    f.close()

    system("msfconsole -q -r Data/{0}/ssh_userEnum.rc -o Output/{}/ssh_userEnum.txt".format(ip))

def ssh_login(ip, port) :
    f = open("ssh_login.rc", "w+")
    f.write("use scanner/ssh/ssh_login\n")
    f.write("set rhosts {}\n".format(ip))
    f.write("set port {\n".format(port))
    f.write("set blank_passwords true\n")
    f.write("set stop_on_success true\n")
    f.write("det pass_file \n") #Set wordlist
    f.write("set user_file \n") #Set wordlist
    f.write("run\n")
    f.write("exit")
    f.close

    system("msfconsole -q -r Data/{0}/ssh_login.rc -o Output/{}/ssh_login.txt".format(ip))

def sshMenu(ip) :

    print('''SSH servie is running on {0}.......

    [1] SSH login
    [2] SSH Version Check (METASPLOIT)
    [3] SSH User Enumeration (METASPLOIT)
    [4] SSH Login Brute-force (METASPLOIT)
    [5] SSH Login Brute_force (HYDRA)
    '''.format(ip))

    option = int(input("Choose an option/options or enter 0 to exit : "))

    nOptions = [int(n) for n in str(option)]

    sshMain(ip, nOptions)


def sshMain(ip, port, nOptions) :
    # try :
    while True :
        for option in nOptions :
            if option == 1 :
                system("ssh -p {1} {0}".format(ip, port))

            if option == 2 :
                print("[~] Scanning the version of SSH. Please Wait..")
                ssh_version(ip, port)
                print("[*] Done")

            elif option == 3 :
                print("Enumeratig")
                ssh_userEnum(ip, port)

            elif option == 4 :
                ssh_login(ip, port)

            elif option == 5 :
                system("hydra -L logins.txt -P pws.txt -M {} ssh".format(ip))

            elif option == 0 or option == '0' :
                print("Exiting...")
                sleep(2)
                sys.exit()
        print("\n")
        sshMenu(ip)

    # except :
    #     sshMenu(ip)
try :
    ip = sys.argv[1]
    port = sys.argv[2]
    sshMenu(ip)

except KeyboardInterrupt :
    print("Eat sleep rave repeat.")
