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
	lineCount = 0
	with open(fileName, 'rb') as file:
		for line in file:
			lineCount = lineCount + 1
	lineChunks = lineCount / len(clients) ##\brief We want our clients to receive a portion of the entire file.
	
	with open(fileName) as file:
			chunkCount = 0
			index = 0
			clients[index].send("SENDFILE")
			for line in file:
				if chunkCount <= lineChunks:
					clients[index].send(str(line))
					chunkCount = chunkCount + 1
				else:
					clients[index].send(str(line))
					if index < len(clients):
						index = index + 1 
						chunkCount = 0
						clients[index].send("SENDFILE")
						print "Heartbeat"
			print "Done sending files"
#Type FILEDONE after you get the command window back.
