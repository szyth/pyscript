#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print('Welcome, This is a simple automation tool')
print('=============================================================')

ip_addr = input('Please input your ip address you want to scan: ')
print('The ip you entered is: ' ,ip_addr)
type(ip_addr)

resp = input("""\n Please enter the type of scan you want to run
                   1)SYN-ACK SCAN
                   2)UDP SCAN
                   3)Comprehensive scan
                   :""")
print('You have selected option: ' ,resp)
if resp =='1':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')       #will scan() the target, built in fn, sS means tcp sleath scan
    print(scanner.scaninfo())                       #display scan results
    print('IP Status: ', scanner[ip_addr].state())   #displays if the host is up or down
    print(scanner[ip_addr].all_protocols())         #since sS thats y tcp is shown in terminal
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys()) #will display open ports
elif resp == '2':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')       #will scan() the target, built in fn, sU for udp
    print(scanner.scaninfo())                       #display scan results
    print('IP Status: ', scanner[ip_addr].state())   #displays if the host is up or down
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['udp'].keys()) #will display open ports    
elif resp == '3':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')       #will scan() the target, sV version detection, A aggresive, O osfingerprint
    print(scanner.scaninfo())                       #display scan results
    print('IP Status: ', scanner[ip_addr].state())   #displays if the host is up or down
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys()) #will display open ports

else:
    print('Print enter the valid option')

    
