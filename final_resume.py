import threading
from threading import Thread
import os
import signal
import subprocess
import time
import sys

import socket
HOST = '10.0.0.3'    # The remote host
PORT = 29999 


pid = -1

def monitor():
    # ping through socket inside while loop
    print 'monitor running'
    global pid
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print ("Received", data)

    i = 1

    while 1:
        if pid != -1:
            i= i+1
            s.send ("safetymode\n")
            data = s.recv(1024)

            if i % 1000 == 0:
                i = 1
                print ("Received", data)

            # a = raw_input('Give commands')
            # if (a == "1"):
                
            if 'PROTECTIVE_STOP' in data:
                print '\n\n\nfuck\n\n\n'
                print 'pid is ' + str(pid)

                s.send ("unlock protective stop\n")
                data = s.recv(1024)
                print ("Received", data)

                s.send ("close safety popup\n")
                data = s.recv(1024)
                print ("Received", data)

                os.killpg(os.getpgid(pid), signal.SIGTERM)  # Send the signal to all the process groups
                time.sleep(2)
                Thread(target = connection_thread).start()

def connection_thread():
    print 'Working'
    global pid
    # The os.setsid() is passed in the argument preexec_fn so
    # it's run after the fork() and before  exec() to run the shell.
    pro = subprocess.Popen(
        "roslaunch apc connect_to_hardware.launch", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid) 
    pid = pro.pid



if __name__ == '__main__':
    Thread(target = monitor).start()
    Thread(target = connection_thread).start()
