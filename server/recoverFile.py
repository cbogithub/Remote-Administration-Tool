#! /usr/bin/env python
##
#\file recoverFile.py
#
#\brief The method to recover a file from the client.
#
#\author Elephant Bomb
#
#\date 2016-04-23

def recoverFile(clients, clientData):
	with open("client_screen.png", 'w') as file:
		file.write(clientData)
		while clientData:
			with open("client_screen.png", 'a') as file:
				file.write(clientData)