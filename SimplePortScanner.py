#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
remoteServer=input("Enter a remote host to scan: ")
remoteServerIP=socket.gethostbyname(remoteServer)

# Banner
print("+" * 60)
print("Scanning remote host", remoteServerIP)
print("+" * 60)

# Check what time the scan started
t1 = datetime.now()

# We also put in some error handling for catching errors

try:
    for port in range(1,65535):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You aborted the scan!")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved!')
    sys.exit()

except socket.error:
    print("Couldn't connect to server!")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print('Scanning Completed in: ', total)