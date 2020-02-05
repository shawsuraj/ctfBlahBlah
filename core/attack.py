class svc:
        def __init__(self, port, open = False):
                self.port = port
                self.open = status


def portScanner(ip, port) :
    print ("[~] Scanning port {0} of {1}".format(port, ip))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = sock.connect_ex((ip,port))
    sock.close()
    if res == 0:
        print("[*] Port {0} in open on {1}".format(port, ip))
        return True
    else :
        return False

def ftp(ip) :
    svc_ftp = svc(21,portScanner(ip,21))
    if svc_ftp.open :
        return "Attacks/ftp.py {}".format(ip)

def ssh(ip) :
    svc_ssh = svc(22,portScanner(ip,22))
    if svc_ssh.open :
        return "Attacks/ssh.py {0} {1}".format(ip, svc_ssh.port)
