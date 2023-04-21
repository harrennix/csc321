import socket
from ipaddress import ip_address

with open('domains.tsv', 'r') as f:
    for line in f:
        domain = line.strip().split('\t')[1].strip()
        try:
            with socket.create_connection((domain, 80), timeout=5) as conn:
                ip = ip_address(conn.getpeername()[1])
                print(f"{domain}: {ip}")
        except (socket.gaierror, socket.timeout):
            print(f"Error: Could not resolve {domain}")


