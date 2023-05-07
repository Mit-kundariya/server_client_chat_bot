# Python program to implement client side of chat room. 

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 5000))
# conn, addr = s.accept()
while 1:
    data = s.recv(1024)
    if not data:
        break
    print(data)
    data=input("enter the data")
    s.sendall(bytes(data,'utf8'))
s.close()