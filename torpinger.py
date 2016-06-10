#!/bin/python3
# Python 3 required !!
# do 'pip3 install pysocks' for socks module

import sys
import socket
try:
    import socks
except ImportError:
    print('Pysocks not installed, do "pip3 install pysocks"')
    print('If pip3 is not installed do "sudo apt-get install python3-pip"')
    sys.exit(1)
try:
    from urllib.request import urlopen
except:
    print('You are not using python3 but just python')
    print('Run the script as "python3 {}"'.format(__file__))
    sys.exit(2)

#### Modify this as per need

# For tor browser port is 9150, for cli of tor, it is 9050
# Set accordingly
SOCKS5_PROXY_PORT = 9050
# interval of time (in seconds) to send request
# should be somewhere b/w 30-60 in final stage
interv = 1
# for each request set timeout
timeout = 10

#### No need to touch after this



# Configuration
SOCKS5_PROXY_HOST = '127.0.0.1'



socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5,addr=SOCKS5_PROXY_HOST,port=SOCKS5_PROXY_PORT)
socket.socket = socks.socksocket


# function to send GET to url
# timeout may be modified suitably
def load_url(url):
    try:
        resp = urlopen(url,timeout=timeout)
        print(resp.read())
        resp.close()
    except OSError:
        print('Time out')


# Important !!

# loop load_p with time interval interv
import time
while True:
    url = 'http://icanhazip.com'
    # Url below is much faster, should be used at final stage
    # url = 'http://www.msftncsi.com/ncsi.txt'
    load_url(url)
    time.sleep(interv)
