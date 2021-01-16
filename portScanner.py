#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)


host = input('Enter the target IP Address: ')
#port = int(input('Enter the port number: '))
portRange = int(input('Enter the Port Range: '))
closedPort = 0
openPort = []


for port in range(0,portRange+1):
    if s.connect_ex((host, port)):
        #print('The Port',port, ' is Closed')
        closedPort+=1
    else:
        openPort.append(port)
print('Closed Ports: ', closedPort)
print('Open Ports: ', openPort)
