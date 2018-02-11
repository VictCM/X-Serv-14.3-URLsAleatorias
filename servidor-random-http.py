#!/usr/bin/python3

import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

mySocket.bind(('localhost', 1264))

#Lo convierto en servidor y digo que solo escuche a 5 clientes como maximo
mySocket.listen(5)

rndm_num=random.randint(1,999999999)

while True:
    print("Waiting for connections")
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received: ')
    print(recvSocket.recv(1024))
    recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                    "<html><body><h1>Hola.</h1>"+
                    "<a href='" + str(rndm_num) + "'> Dame otra </a>\r\n"+
                    "</body></html>"+
                    "\r\n")
    recvSocket.close()
