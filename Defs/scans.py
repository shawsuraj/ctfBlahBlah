import os

# DEBUG: Find a way to make the verbose option work other than passing it in every function.
verbose = True

#FIREFOX
def firefox(ip) :
    firefox_cmnd = 'firefox -new-tab -url http://{0}/ -new-tab -url http://{0}/robots.txt'.format(ip)
    # Verbose
    if verbose :
        print("> Opening http://{0}/ &  http://{0}/robots.txt in firefox".format(ip))
    return firefox_cmnd

#NMAP
def nmap_scan(ip) :
    nmap_cmnd = 'nmap -v -A {0} -oN Output/{0}/nmap.txt'.format(ip)
    # Verbose
    if verbose :
        print("> Starting nmap scan on {0}".format(ip))
    return nmap_cmnd

#DIRB
def dirb_scan(ip) :
    dirb_cmnd = 'dirb http://{0} -o Output/{0}/dirb.txt'.format(ip)
    # Verbose
    if verbose :
        print("> Starting dirb scan on {0}".format(ip))
    return dirb_cmnd

#WPSCAN
def wp_scan(ip) :
    if not os.system('curl -s --head http://{}/wp-login | head -n 1 | grep "HTTP/1.[01] [23].." > /dev/null '.format(ip)) :
    # if not os.system('curl --output /dev/null --silent --head --fail "http://{}/wp-login" '.format(ip[i])) :   #Better way
        wp_cmnd =  'wpscan -v --url {0} -e u -o Output/{0}/wpscan.txt'.format(ip)
        # Verbose
        if verbose :
            print("> Starting wp-scan on {0}".format(ip))
    else :
        return

    exec(wp_cmnd)

#SQLI
def sql_scan():
    sqlUrl = list()
    varS = 1
    while varS :
        varS = input("Enter the Url for Sql Injection. Enter 0 to exit : ")
        if not (varS == 0 or varS == '0'):
            sqlUrl.append(varS)
            print(varS)
        else :
            break

    print(sqlUrl)
    print(len(sqlUrl))

    if(len(sqlUrl)) :
        if sqlCheck(*sqlUrl) :
            sqlI(*sqlUrl)
        else :
            return
    else :
        return
