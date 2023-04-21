import socket

# Define a list of domains to resolve
domains = ['google.com', 'facebook.com', 'example.com', 'nonexistentdomain12345.com']

# Loop through the list of domains
for domain in domains:
    try:
        # Forward DNS lookup for the domain name
        ip_addresses = socket.getaddrinfo(domain, None)
        # Loop through each IP address associated with the domain
        for ip_address in ip_addresses:
            try:
                # Reverse DNS lookup for the IP address
                reverse_dns = socket.gethostbyaddr(ip_address[4][0])
                # Print the IP and hostname
                print(f"{ip_address[4][0]}: {reverse_dns[0]}")
            except socket.herror:
                print(f"Error: No reverse DNS record could be found for {ip_address[4][0]}")
    except socket.gaierror:
        print(f"Error: Could not resolve {domain}")