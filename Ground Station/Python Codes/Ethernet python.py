# Echo client program
# The arduino is the "server"
import socket

def send_ether(MESSAGE)
    HOST = ''               # The arduino ip address 
    PORT = #port            # The same port as used by the arduino
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall('MESSAGE')           # Need to decide what to send to arduino 
    data = s.recv(1024)     # Recieved data maybe confirmation from arduino 
    s.close()               
