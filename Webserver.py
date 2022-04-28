import socket
serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSock.bind(('127.0.0.1',6789))

while True:
    data,addr = serverSock.recvfrom(4096)
    print(str(data))
    message = bytes("Hello this is the UDP server").encode('utf-8')
    serverSock.sendto(message,addr)