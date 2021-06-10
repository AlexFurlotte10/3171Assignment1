#import socket module 
from socket import *
import sys # in order to terminate the program
serverPort=6789
serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare a server socket
#Fill in start
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Get served! at ", serverPort)
#Fill in end
while True:
    #establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end

    try:
        message = connectionSocket.recv(1024)#Fill in start #fill in end
        print(message,'::',message.split()[0],':',message.split()[1])
        filename = message.split()[1]
        print(filename,'||',filename[1:])
        f = open(filename[1:])
        outputdata = f.read()#Fill in start #fill in end
        #send one HTTP header line into socket
        #Fill in start
        print(outputdata)
        connectionSocket.send(bytes('\nHTTP/1.1 200 OK\n\n', encoding='utf8'))
        connectionSocket.send(bytes(outputdata, encoding= 'utf8'))
        #Fill in end
        #send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(bytes(outputdata[i], encoding='utf8'))
            connectionSocket.send(bytes("r\n", encoding='utf8'))
            connectionSocket.close()
    except IOError:
            #send response message for file not found
            #fill in start
        connectionSocket.send(bytes("\nHTTP/1.1 404 Not Found\n\n", encoding='utf8'))
            #fill in end
            #close client socket
            #fill in start
            #fill in end
        serverSocket.close()
        sys.exit()#terminate the program after sending the corresponding data