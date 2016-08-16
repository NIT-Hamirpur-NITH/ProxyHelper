#!/usr/bin/python3

# bing.com is only here for testing purpose, have to remove it
FAST_DOMAIN = 'bing.com'
proxies = ['{}'.format(FAST_DOMAIN),'172.16.24.2',
           '172.16.24.3','172.16.24.4','172.16.12.2','172.16.12.3',
           '172.16.20.2','172.16.28.11','172.16.32.2']

print('-'*30)
print('Searching for best proxy ...')
print('-'*30)
print('')
print('  -> Available: {}\n'.format(proxies))
import sys
import subprocess
import random
import threading
import logging
import time
import re

INFI = float('inf')

# logging.basicConfig(level=logging.DEBUG,
                    # format='(%(threadName)-9s) %(message)s',)
pidi = {}

class Pinger(object):
    def __init__(self,name=None):
        self.name = name
        self.pattern = re.compile(r'rtt min/avg/max/mdev = (.*?)/(.*?)/(.*?)/(.*?) .*$')

    def ping(self,proxy):
        # logging.debug('Class name {}'.format(self.name))
        self.proxy = proxy
        self.op = subprocess.check_output('ping -c4 -w4 {} 2>/dev/null | tail -1'.format(self.proxy),shell=True)
        self.op_clean()
        # print('Output is {}'.format(self.op))
        return self.op

    def op_clean(self):
        self.op = self.op.strip()
        self.op = self.op.decode()
        if len(self.op)==0:
            self.op =  INFI
            return
        # output is of the form : min/avg/max/mdev
        match = self.pattern.match(self.op)
        if match == None:
            # logging.debug('Pattern not matched! exiting')
            sys.exit(1)
        self.op = match.group(2) # avg is index 2 group
        self.op = float(self.op)

class PingThread(threading.Thread):

    def __init__(self,target=None,pinger=Pinger(),args=None):
        super().__init__()
        self.target = target
        self.pinger = pinger
        self.arg = args[0]

    def run(self):
        # logging.debug('Created thread')
        self.target(self.arg,self.pinger)

def target(proxy,pinger):
    pidi[proxy]=pinger.ping(proxy)
    # logging.debug('Handling task {}'.format(pidi))

if __name__ == '__main__':
    main_t = threading.currentThread()
    time_init = time.time()
    thread_c = len(proxies)
    pinger = Pinger('original')
    # logging.debug('Threads created {}'.format(thread_c))
    print('  -> Pinging them all in parallel\n')
    for p in proxies:
        th = PingThread(target=target,pinger=pinger,args=(p,))
        th.start()
    for t in threading.enumerate():
        if t is not main_t:
            t.join()

    # pinger.ping(proxies[random.randint(0,len(proxies)-1)])
    # logging.debug('Time taken for resolution = {}'.format(time.time()-time_init))

    # select best proxy
    # python 2 has no items() but iteriterms()
    best_p = min(pidi.items(),key=lambda x: x[1])
    if best_p[1] == INFI or best_p[0] == FAST_DOMAIN:
        print('  -> Cannot identify proxy; Clearing proxy;')
        sys.exit()
    else:
        print('  -> Best proxy : {}'.format(best_p[0]))
    

