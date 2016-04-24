#! /usr/bind/env python
##
#\brief fileSend function reads the contents of output.txt then sends it to the clients in chunks.
#\param fileName accepts a path to a file.
#\param clients accepts a list of connected clients.
#\details Use 'SENDFILE' to initiate the client.
#
def fileSend(fileName, clients):
	fileData = []
	with open(fileName) as file:
		fileContent = file.read()
		fileData.append(fileContent)
	for i in range(0, len(clients)):
		clients[0].send("SENDFILE")
		clients[0].send(str(fileContent))
		#Type FILEDONE after you get the command window back.

def incomingFile(data, socketHolder):
	print data
	nextData = socketHolder.recv(1024)
	while nextData:
		if nextData == "FILEDONE": 
			break
		else:
			with open("client_dictionary.txt", 'w') as file:
				file.write(nextData)
			nextData = socketHolder.recv(1024)