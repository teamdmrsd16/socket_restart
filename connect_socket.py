# Echo client program
import socket
HOST = '10.0.0.3'    # The remote host
PORT = 29999              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
print ("Received", data)

####
s.send ("running\n")
data = s.recv(1024)
print ("Received", data)

####
s.send ("robotmode\n")
data = s.recv(1024)
print ("Received", data)

####
s.send ("close popup\n")
data = s.recv(1024)
print ("Received", data)

####
s.send ("close safety popup\n")
data = s.recv(1024)
print ("Received", data)

####
s.send ("safetymode\n")
data = s.recv(1024)
print ("Received", data)


if 'PROTECTIVE_STOP' in data:
    print 'fuck'

####
# s.send ("unlock protective stop\n")
# data = s.recv(1024)
# print ("Received", data)

s.close()
