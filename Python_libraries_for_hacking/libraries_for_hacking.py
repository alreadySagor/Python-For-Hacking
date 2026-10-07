"""
1. Socket (Networking)
2. Scapy (packet crafting/sniffing)
3. Requests (web scraping and HTTP requests)
4. Hashlib (hashing alogorithms for password security)
"""

import socket
def port_scanner(target, port_range):
    print(f"scanning {target}...")
    for port in range(*port_range):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # this is a socket object
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"port {port} is OPEN")
            s.close()
        except Exception as e:
            print(f"ERROR SCANNING {port}: {e}")

target = "127.0.0.1"
port_range = (20, 25)
port_scanner(target, port_range)