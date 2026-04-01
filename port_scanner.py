import socket
import threading
from datetime import datetime

# Configuration & Logging setup
LOG_FILE = "scan_results.txt"

def log_result(message):
    print(message)
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

def scan_port(host, port):
    """Attempts to connect to a specific port on a host."""
    try:
        # Create a TCP socket
        # AF_INET = IPv4, SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout so we don't wait forever on filtered ports
        s.settimeout(1.0)
        
        # connect_ex returns an error indicator (0 for success)
        result = s.connect_ex((host, port))
        
        if result == 0:
            log_result(f"[+] Port {port}: OPEN")
        else:
            # Uncomment the line below if you want to log closed ports too
            # log_result(f"[-] Port {port}: CLOSED/FILTERED")
            pass
            
        s.close()
    except Exception as e:
        log_result(f"[!] Error scanning port {port}: {e}")

def main():
    target = input("Enter the host to scan (e.g., 127.0.0.1 or google.com): ")
    
    # Simple input handling for port ranges
    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
    except ValueError:
        print("Please enter valid port numbers.")
        return

    # Resolve hostname to IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Hostname {target} could not be resolved.")
        return

    print("-" * 50)
    print(f"Scanning Target: {target_ip}")
    print(f"Time Started: {datetime.now()}")
    print("-" * 50)

    threads = []

    # Concurrency: Spawning a thread for each port scan
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("-" * 50)
    print(f"Scan Completed. Results saved to {LOG_FILE}")

if __name__ == "__main__":
    main()