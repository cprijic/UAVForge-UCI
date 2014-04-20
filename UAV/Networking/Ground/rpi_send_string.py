import socket


HOST = '192.168.1.100'               # The rPi ip address 
PORT = 8888	                     # The port number 


s = socket.socket() 
s.connect((HOST, PORT))

s.sendto(bytes(' '),(HOST,PORT))


while True:
    received = (s.recv(1024))
    print received
    send =  raw_input('What do you want to send?: ')
    if send == 'shutdown':
        break
    else:
        s.sendto(send,(HOST,PORT))
    
s.close()
        

