#! /usr/bin/env python
##
#\file client_setup.py
#
#\brief The setup file to turn client.py to an .exe
#
#\author Elephant Bomb
#
#\date 2016-04-20
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "client.py"}],
    zipfile = None,
)

