import socket
import ftplib
import sys

def check_port(ip, port, timeout=1):
    """Checks if a specific port is open on the target IP."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            return True
        else:
            return False
    except socket.error:
        return False
    finally:
        sock.close()

def check_anonymous_ftp(ip):
    """Attempts an anonymous FTP login on the target IP."""
    print(f"[*] Attempting anonymous FTP login on {ip}:21...")
    try:
        with ftplib.FTP(ip, timeout=5) as ftp:
            ftp.login('anonymous', 'anonymous@example.com') # Common anonymous login credentials
            print(f"[+] Anonymous FTP login successful on {ip}!") # Vulnerability found!
            print("    Listing root directory (first 5 items):")
            try:
                ftp.dir(lambda x: print(f"    - {x}"), '-a') # List directory contents
            except Exception as e:
                print(f"    Could not list directory: {e}")
            return True
    except ftplib.all_errors as e:
        print(f"[-] Anonymous FTP login failed on {ip}: {e}")
        return False
    except socket.error as e:
        print(f"[-] Could not connect to FTP on {ip}: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python recon_scanner.py <TARGET_IP>")
        sys.exit(1)

    target_ip = sys.argv[1]
    print(f"[*] Starting basic reconnaissance on {target_ip}")

    # Common ports to check for initial reconnaissance
    common_ports = {
        21: "FTP",
        22: "SSH",
        80: "HTTP",
        139: "NetBIOS-SSN (SMB)",
        445: "Microsoft-DS (SMB)"
    }

    open_ports = []
    for port, service in common_ports.items():
        print(f"[*] Checking port {port} ({service})...")
        if check_port(target_ip, port):
            print(f"[+] Port {port} ({service}) is OPEN")
            open_ports.append(port)
        else:
            print(f"[-] Port {port} ({service}) is CLOSED")

    print("\n--- Reconnaissance Summary ---")
    print(f"Target IP: {target_ip}")
    if open_ports:
        print(f"Open Ports: {', '.join(map(str, open_ports))}")
    else:
        print("No common ports found open.")

    # If FTP port is open, proceed with vulnerability check
    if 21 in open_ports:
        print("\n--- Vulnerability Check: Anonymous FTP ---")
        check_anonymous_ftp(target_ip) # Illustrates identifying a common vulnerability

    print("\n[*] Reconnaissance and basic vulnerability check complete.")

if __name__ == "__main__":
    main()
