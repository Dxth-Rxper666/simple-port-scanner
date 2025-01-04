import socket
import sys
from datetime import datetime
import threading

def scan_port(target, port):
    try:
        # Create socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # Try to connect to port
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.gaierror:
        print("\nHostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\nServer not responding.")
        sys.exit()

def main():
    # Get target from user
    target = input("Enter target IP address: ")
    
    # Print banner
    print("-" * 50)
    print(f"Scanning target: {target}")
    print(f"Scan started at: {str(datetime.now())}")
    print("-" * 50)

    try:
        # Scan ports 1-1024
        threads = []
        for port in range(1,1025):
            thread = threading.Thread(target=scan_port, args=(target, port))
            thread.start()
            threads.append(thread)

        # Wait for all threads to complete    
        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("\nExiting Program.")
        sys.exit()

if __name__ == "__main__":
    main()
