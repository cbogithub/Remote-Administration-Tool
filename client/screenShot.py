#! /usr/bin/env python
##
#\file screenShot.py
#
#\brief The method to take a screen shot of the screen.
#
#\author Elephant Bomb
#
#\date 2016-04-24
from PIL import ImageGrab

def screenShot():
	imageGrab = ImageGrab.grab()
	imageGrab.save('client_screen.png')