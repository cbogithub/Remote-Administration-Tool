#! /usr/bin/env python
##
#\file incomingFile.py
#
#\brief The method to write to a dictionary file.
#
#\author Elephant Bomb
#
#\date 2016-04-23

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