#! /usr/bin/env python
##
#\file openZip.py
#
#\brief The zip opener
#
#\author Elephant Bomb
#
#\date 2016-04-24
import zipfile

def openZip():
	zipFile = zipfile.ZipFile('secrets.zip')
	dictionary = open('client_dictionary.txt')
	for eachLine in dictionary.readlines():
		password = eachLine.strip('\n')
		try:
			zipFile.extractall(pwd=password)
			return password
		except Exception, e:
			pass