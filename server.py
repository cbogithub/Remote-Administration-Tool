#!/usr/bin/python
from socket import *
HOST = ''       
PORT = 22       

socketHandler = socket(AF_INET, SOCK_STREAM)

socketHandler.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

socketHandler.bind((HOST, PORT))

print "Listening on PORT: %s" % str(PORT)

socketHandler.listen(10) #Accepting 10 Connections

connection, address = socketHandler.accept()

print 'Welcome: ', address

firstClientData = connection.recv(1024)

print firstClientData

while True:
     commandClient = raw_input("Enter a command or type 'quit': ")

     connection.send(commandClient)

     if commandClient == "quit": break

     clientData = connection.recv(1024)

     print clientData

connection.close()
