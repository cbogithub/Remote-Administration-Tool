
#!/usr/bin/python
##
#\file server.py
#
#\brief The server for our Remote Administration Tool
#
#\author Elephant Bomb
#
#\date 2016-04-10
from socket import *
import sys
import thread
HOST = ''       
PORT = 22

def fileSend(fileName, clients):
	fileData = []
	with open(fileName) as file:
		fileContent = file.read()
		print fileContent
		fileData.append(fileContent)
	for i in range(0, len(clients)):
		clients[0].send("SENDFILE")
		clients[0].send(str(fileContent))

def sendMessages(clients):
	while True:
		if clients:
			commandClient = raw_input("Enter a command: ")
			if commandClient == "SENDFILE":
				fileName = "C:\output.txt"
				fileSend(fileName, clients)
			else:
				for i in range(0, len(clients)):
					clients[i].send(commandClient)
	clients.close()

def handleMessages(clients):
	while True:
		for i in range(0, len(clients)):
				clientData = clients[i].recv(1024)
				if clientData:
					print clientData
	clients.close()

if __name__=='__main__':
	#Create a container for clients
	clients = []
	#Create and bind sockets
	socketHandler = socket(AF_INET, SOCK_STREAM)
	socketHandler.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	socketHandler.bind((HOST, PORT))
	print "Listening on PORT: %s" % str(PORT)
	#Accepting 20 Connections to Queue
	socketHandler.listen(20) 
	while True:
		connection, address = socketHandler.accept()
		print 'Connection from: ', address
		clients.append(connection)
		thread.start_new_thread(sendMessages, (clients,))
		thread.start_new_thread(handleMessages, (clients,))