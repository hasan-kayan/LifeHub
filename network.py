import nmap

def scan_network(network):
    # Create a new nmap scanner object
    scanner = nmap.PortScanner()

    # Scan the specified network
    scanner.scan(hosts=network, arguments='-sn')

    # Iterate over the scanned hosts
    for host in scanner.all_hosts():
        # Get the MAC address of the host
        mac_address = scanner[host]['addresses']['mac']
        print(f"Host: {host}\tMAC Address: {mac_address}")

        # Check for open ports on the host
        port_scanner = scanner.scan(hosts=host, arguments='-p 1-1000')
        open_ports = []

        # Iterate over the scanned ports
        for port in port_scanner[host]['tcp']:
            if port_scanner[host]['tcp'][port]['state'] == 'open':
                open_ports.append(port)

        # Print open ports if any
        if open_ports:
            print(f"Open Ports: {', '.join(map(str, open_ports))}")
        else:
            print("No open ports found")

# Specify the network you want to scan (e.g., '192.168.0.0/24')
network_to_scan = input("Enter the network you want to scan: ")

# Perform the network scan
scan_network(network_to_scan)
