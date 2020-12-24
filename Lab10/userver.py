import socket
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('LAPTOP-848O6A2G', serverPort))
print ("The server is ready to receive")
while 1:
     sentence,clientAddress = serverSocket.recvfrom(2048)

     file=open(sentence,"r")
     l=file.read(2048)

     serverSocket.sendto(bytes(l,"utf-8"),clientAddress)
     print("sent back to client",l)
     file.close()
