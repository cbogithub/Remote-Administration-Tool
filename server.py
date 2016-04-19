
#!/usr/bin/python
from socket import *
import sys
import thread
HOST = ''       
PORT = 22

def sendMessages(connection, quit):
	while True:
		commandClient = raw_input("Enter a command: ")
		connection.sendall(commandClient)
		if commandClient == "exit":
			break
	connection.close()

def handleMessages(connection, quit):
	while True:
		clientData = connection.recv(1024)
		print clientData
		if clientData == "exit":
			break
	connection.close()

if __name__=='__main__':
	quit = False
	#Create and bind socket
	socketHandler = socket(AF_INET, SOCK_STREAM)
	socketHandler.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	socketHandler.bind((HOST, PORT))
	print "Listening on PORT: %s" % str(PORT)
	#Accepting 10 Connections
	socketHandler.listen(10) 
	while True:
		connection, address = socketHandler.accept()
		print 'Connection from: ', address
		thread.start_new_thread(sendMessages, (connection, quit))
		thread.start_new_thread(handleMessages, (connection, quit))