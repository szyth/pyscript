#!usr/bin/python3

import socket

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

clientSock.connect((host, port))

msg = clientSock.recv(1024)

clientSock.close()

print(msg.decode('ascii'))