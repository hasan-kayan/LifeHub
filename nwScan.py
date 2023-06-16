from scapy.all import ARP, Ether, srp

def scan_network(interface):
    # Create an ARP request packet
    arp = ARP(pdst='192.168.1.1/24')
    ether = Ether(dst='ff:ff:ff:ff:ff:ff')
    packet = ether / arp

    # Send the packet and capture the response
    result = srp(packet, timeout=3, iface=interface, verbose=0)[0]

    # Process the response
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    # Print the list of devices
    print('Devices on the network:')
    print('----------------------')
    for device in devices:
        print(f'IP: {device["ip"]}   MAC: {device["mac"]}')


