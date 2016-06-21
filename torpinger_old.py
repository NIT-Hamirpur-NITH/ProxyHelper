#!/usr/bin/python3
# Python 3 required !!
# do 'pip3 install pysocks' for socks module

import sys
import socket
import subprocess
import time
try:
    import socks
except ImportError:
    print('Pysocks not installed, do "pip3 install pysocks"')
    print('If pip3 is not installed do "sudo apt-get install python3-pip"') 
    print('On older versions of Ubuntu it is possible that python3 is not installed\n\ Look up google for that')
    sys.exit(1)
try:
    from urllib.request import urlopen
except:
    print('You are not using python3 but just python')
    print('Run the script as "python3 {}"'.format(__file__))
    sys.exit(2)


class TorPinger(object):
    def __init__(self):
        #### All configurable parts are listed below
        # TO add
        possible_sockets = [9050,9150]
        ## If multiple tor sockets are found active
        ## One with higher priority is selected
        ## Default behaviour is to prioritize tor-browser socket(9150) over
        ## tor-terminal socket(9050); if you are not sure, leave as it is
        priority = [1,2]
        ## Comment the first url and uncomment 2nd url at production
        # self.ping_url = 'http://icanhazip.com'
        self.ping_url = 'http://www.msftncsi.com/ncsi.txt'
        ## time between two pings
        ## should be 30seconds ??
        self.interval = 30
        ## timeout for one ping
        ## should be 5 seconds ??
        self.timeout = 5
        ## If program doesn't find any active tor connection within these seconds, it
        ## will stop its operation and exit
        self.timeout_for_socks = 3
        ## time it will wait to check if there is some update or note, no need to modify
        self.timeout_one_check = 1

        #### Do not modify below this 
        ## Stores the socket of connection which I want to torping
        self.SOCK_REAL = None
        self.sockets = dict(zip(possible_sockets,priority))
    
    def set_socket(self,SOCKS5_PROXY_PORT):
        SOCKS5_PROXY_HOST = '127.0.0.1'
        socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5,addr=SOCKS5_PROXY_HOST,port=SOCKS5_PROXY_PORT)
        socket.socket = socks.socksocket

    def ping_socket(self,url):
        ## function to send GET to url
        try:
            resp = urlopen(url,timeout=self.timeout)
            print(resp.read())
            resp.close()
        except OSError:
            print('Time out')

    def which_socks(self):
        op = subprocess.check_output('netstat -lnt',shell=True).decode()
        SOCKS = []
        for SOCK in self.sockets:
            success = False
            ## Comment below later
            # print(op.find(str(SOCK)))
            ## If socket is open
            if op.find(str(SOCK)) != -1:
                SOCKS.append(SOCK) 
        print(SOCKS)
        return SOCKS
    
    def main_loop(self):
        initT = time.time()
        while time.time()-initT < self.timeout_for_socks:
            SOCKS=self.which_socks()
            time.sleep(self.timeout_one_check)
        ## If we get away from loop due to timeout, then exit
        if len(SOCKS) == 0:
            print('Sorry dude couldn\'t find any active tor connection in the\
                    given time, exitting')
            sys.exit(4)
        ## Else we are good to go and have a list of open tor sockets
        ## Of which we choose the one with highest priority
        self.SOCK_REAL = max(SOCKS, key=lambda x: self.sockets[x])
        ## Only req for testing purpose
        ## You can open the below file side by side
        ## to see automatic operation in action
        # f = open('/tmp/tortester','a')
        # f.write(time.ctime())
        # f.write(' PORT: '+str(self.SOCK_REAL)+'\n')
        # f.close()

        print('highest priority socks',self.SOCK_REAL)
        ## Now we have the socket, so we
        ## set the socket
        self.set_socket(self.SOCK_REAL)
        ## and ping the socket
        while True:
            self.ping_socket(self.ping_url)
            time.sleep(self.interval)

if __name__=='__main__':
    tpinger = TorPinger()
    # tpinger.main_loop()
    tpinger.which_socks()



