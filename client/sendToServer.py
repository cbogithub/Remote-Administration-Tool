#! /usr/bin/env python
##
#\file sendToServer.py
#
#\brief The method to send a file to the server.
#
#\author Elephant Bomb
#
#\date 2016-04-25

##
#\brief sendToServer function reads the contents of output.txt then sends it to the clients in chunks.
#\param fileName accepts a path to a file.
#\param socketHolder accepts a socket.
#\details Use 'RECOVERFILE' to initiate the client.
#
def sendToServer(fileName, socketHolder):
	socketHolder.send("RECOVERFILE")
	fileName = open(fileName, "rb")
	line = fileName.read(1024)
	while(line):
		socketHolder.send(line)
		line = fileName.read(1024)
	fileName.close()