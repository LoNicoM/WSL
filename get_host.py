#!/usr/bin/python3

import subprocess
import re

ip_addr = subprocess.getoutput("ip addr")  # get the output of 'ip addr'
ip = re.findall(r"inet (1[79]\d.\d{1,3}.\d{1,3}.\d{1,3})/20", ip_addr)[0].split(".") # use regex to extract the ip address
ip = int.from_bytes([int(i) for i in ip], "big")  # str to int and then convert bytes to int 
mask = 4294963200  # /20 subnet mask as an integer 
ip_first = int.to_bytes((ip & mask) + 1, 4, "big")  # first host = (ip address & mask) + 1

print(f"{ip_first[0]}.{ip_first[1]}.{ip_first[2]}.{ip_first[3]}")  # print host address
