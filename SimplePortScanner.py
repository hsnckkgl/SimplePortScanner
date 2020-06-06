import sys
import socket
from datetime import datetime

# Target definition
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Hostname translation to IPv4
else:
    print("Invalid amount of argument!")
    print("Syntax: python3 SimplePortScanner.py <IP>")

print("#" * 60)
print("Scanning target " + target)
print("Time Started: " + str(datetime.now()))
print("#" * 60)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open.".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program!")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved!")
    sys.exit()

except socket.error:
    print("Could not connect to server!")
    sys.exit()