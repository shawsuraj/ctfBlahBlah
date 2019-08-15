import os
import sys
import re
import urllib

#Vebose
for arg in sys.argv :
    if arg == "-v" : #If true - show verbose
        verbose = True
    elif not arg == "-v" :
        verbose = False

#FIREFOX
def firefox(site) :
    firefox_cmnd = 'firefox -new-tab -url http://{0}/ -new-tab -url http://{0}/robots.txt'.format(site)
    # Verbose
    if verbose :
        print("[*] Opening http://{0}/ &  http://{0}/robots.txt in firefox".format(site))
    return firefox_cmnd

#NMAP
def nmapScan(site) :
    nmap_cmnd = 'nmap -v -p 0-65535 -sSVC {0} -oN Output/{0}/nmap.txt'.format(site)
    # Verbose
    if verbose :
        print("[*] Starting nmap scan on {0}".format(site))
    return nmap_cmnd

#DIRB
def dirbScan(site) :
    dirb_cmnd = 'dirb http://{0} -o Output/{0}/dirb.txt'.format(site)
    # Verbose
    if verbose :
        print("[*] Starting dirb scan on {0}".format(site))
    return dirb_cmnd

#WPSCAN
def wpScan(site) :
    print ("[~] Checking wordpress on {}".format(site))
    # if urllib.urlopen(site + 'wp-login').getcode() == 200:
    if not os.system('curl -s --head http://{}/wp-login | head -n 1 | grep "HTTP/1.[01] [23].." > /dev/null '.format(site)) :
    # if not os.system('curl --output /dev/null --silent --head --fail "http://{}/wp-login" '.format(site[i])) :   #Better way
        print("[*] Found")
        wp_cmnd =  'wpscan -v --url {0} -e u -o Output/{0}/wpscan.txt'.format(site)
        # Verbose
        if verbose :
            print("[*] Starting wp-scan on {0}".format(site))
    else :
        return

    return wp_cmnd

#Get Files
def wget(site) :
    wget_cmnd = 'wget http://{0}/robots.txt -O Output/{0}/robots.txt'.format(site)

    return wget_cmnd

#SQLI
# def sql_scan():
#     sqlUrl = list()
#     varS = 1
#     while varS :
#         varS = input("Enter the Url for Sql Injection. Enter 0 to exit : ")
#         if not (varS == 0 or varS == '0'):
#             sqlUrl.append(varS)
#             print(varS)
#         else :
#             break
#
#     print(sqlUrl)
#     print(len(sqlUrl))
#
#     if(len(sqlUrl)) :
#         if sqlCheck(*sqlUrl) :
#             sqlI(*sqlUrl)
#         else :
#             return
#     else :
#         return
