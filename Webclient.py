import socket
clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message = "Hello UDP Server"
clientSock.sendto(message.encode("utf-8"),('127.0.0.1'))

data,addr = clientSock.recvfrom(4096)
print("Server Says")
print(str(data))
clientSock.close()