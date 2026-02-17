# from stack overflow, not working...

import os
import time 
from subprocess import Popen, DEVNULL

p = {} # ip -> process
for n in range(1, 100): # start ping processes
    ip = "192.168.1.%d" % n
    p[ip] = Popen(['ping', '-n', '-w5', '-c3', ip], stdout=DEVNULL)
    #NOTE: you could set stderr=subprocess.STDOUT to ignore stderr also
print(p)

while p:
    for ip, proc in p.items():
        if proc.poll() is not None: # ping finished
            del p[ip] # remove from the process list
            if proc.returncode == 0:
                print('%s active' % ip)
            elif proc.returncode == 1:
                print('%s no response' % ip)
            else:
                print('%s error' % ip)
            break