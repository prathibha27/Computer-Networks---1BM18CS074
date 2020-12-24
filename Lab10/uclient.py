import socket
serverName = 'LAPTOP-848O6A2G'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sentence = input("Enter file name")
clientSocket.sendto(bytes(sentence,"utf-8"),(serverName, serverPort))
filecontents,serverAddress = clientSocket.recvfrom(2048)
print ('From Server:', filecontents)

clientSocket.close()
