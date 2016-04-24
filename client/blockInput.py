#! /usr/bin/env python
import pythoncom
import pyHook

def setBlock(event):    
    return False   

def blockInput():    
    hookManager = pyHook.HookManager()    
    hookManager.MouseAll = setBlock    
    hookManager.KeyAll = setBlock    
    hookManager.HookMouse()    
    hookManager.HookKeyboard()    
    pythoncom.PumpMessages()

blockInput()    