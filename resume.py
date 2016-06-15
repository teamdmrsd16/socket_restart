import threading
from threading import Thread
import os
import signal
import subprocess
import time
import sys


pid = -1

def monitor():
    # ping through socket inside while loop
    print 'monitor running'
    global pid
    while 1:
        if pid != -1:
            a = raw_input('Give commands')



            if (a == "1"):
                print 'pid is ' + str(pid)
                os.killpg(os.getpgid(pid), signal.SIGTERM)  # Send the signal to all the process groups
                # time.sleep(1)
                # thread.exit()
                # sys.exit()


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
