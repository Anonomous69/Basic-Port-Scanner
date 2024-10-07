import socket
import subprocess
from _datetime import datetime

target = input("Enter the target IP address")

def port_scan(target):
    try:
        ip = socket.gethostbyname(target)

        print(f"Scanning the target {ip}")
        print(f"Time started:", datetime.now())

        for port in range(20, 8000):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} Open")
            sock.close()

    except socket.gaierror:
        print(f"Invalid IP address: {target}")

    except socket.error:
        print("Unable to connect to the network")


port_scan(target)