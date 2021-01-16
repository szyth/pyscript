
#!usr/bin/python

import socket

#creating socket object
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname
port = 444

#binding to socket
serverSock.bind(('192.168.29.154', port)) #host will be substituted with ip, if changed and not running on host

#starting TCP listener
serverSock.listen(3)

while True:
    #starting the connection
    clientSock, address = serverSock.accept()
    print('Connection established with %s' % str(address))

    msg = 'Hello welcome to the server' + "\r\n"
    clientSock.send(msg.encode('ascii'))
    clientSock.close()