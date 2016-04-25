#! /usr/bin/env python
##
#\file blockInput.py
#
#\brief The input blocker
#
#\author Elephant Bomb
#
#\date 2016-04-10
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