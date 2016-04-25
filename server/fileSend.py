#! /usr/bin/env python
##
#\file fileSend.py
#
#\brief The method to read a dictionary file and send it to the client.
#
#\author Elephant Bomb
#
#\date 2016-04-23

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
		clients[i].send("SENDFILE")
		clients[i].send(str(fileContent))
		#Type FILEDONE after you get the command window back.
