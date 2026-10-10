import socket
import threading

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[*] port {port} is open")
        s.close()
    except Exception as z:
        print(f"[-] Error scanning port {port} : {z}")

def scan_porst(ip, ports):
    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

target_ip = "127.0.0.1"
portstoscan = range(1, 1025)
print(f"Scanning {target_ip} for open ports...\n")
scan_porst(target_ip, portstoscan)
print(f"\nScanning complete!")