#!/usr/bin/python3


import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


mySocket.bind(('localhost', 1234))


mySocket.listen(5)

try:
    while True:
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('Request received:')
        print (recvSocket.recv(2048).decode("utf-8", "strict"))
        print ('Answering back...')
        random_int = str(random.randint(99999,999999))
        recvSocket.send(bytes("HTTP/1.1 303 See Other\r\n\r\n" +
                              "<html><body><h1>" +
                              "<meta http-equiv='refresh' content= 3;url=/" +
                              random_int + "/>Redirigiendo a... /" +
							  random_int + "</h1></body></html>"
                              "\r\n", "utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print ("Closing binded socket")
mySocket.close()