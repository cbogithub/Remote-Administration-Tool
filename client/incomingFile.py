#! /usr/bin/env python
##
#\file incomingFile.py
#
#\brief The method to write to a dictionary file.
#
#\author Elephant Bomb
#
#\date 2016-04-23

def incomingFile(socketHolder):
	nextData = socketHolder.recv(1024)
	while nextData:
		if nextData == "FILEDONE": 
			break
		else:
			with open("client_dictionary.txt", 'a') as file: ##\brief Use 'w' to write over a file and 'a' to append a file.
				file.write(nextData)
				print nextData
			nextData = socketHolder.recv(1024)