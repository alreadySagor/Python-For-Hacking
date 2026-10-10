import socket

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[*] port {port} is open on {target}")
        else:
            print(f"[-] port {port} is closed on {target}")
        s.close()
    except Exception as z:
        print(f"Error scanning port (port): {z}")
target_ip = "127.0.0.1"
for port in range(20, 1025):
    scan_port(target_ip, port)