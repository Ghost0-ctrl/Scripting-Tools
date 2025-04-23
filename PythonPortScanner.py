# Python Port Scanner
# This is a basic port scanner that searches for open ports upon entering an IP address.


import socket
from datetime import datetime

def scan_ports(target, port_range):
    print(f"Starting scan on {target}")
    print(f"Time started: {datetime.now().strftime('%H:%M:%S')}")
    
    try:
        for port in port_range:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN... Toyota F**kin Supra!!!")
            s.close()
    except KeyboardInterrupt:
        print("\nScan aborted.")
    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Could not reconnect to server.")
        
# Example Usage:
if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    ports = range(1, 1025)
    scan_ports(target, ports)
    
    
    
