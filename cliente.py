#!/usr/bin/python
from socket import *

host = 'localhost'
port = 52000

sock = socket()
sock.connect((host, port))

while True:
    data = sock.recv(1024)
    print data
    sock.send('cliente1')

sock.close()
