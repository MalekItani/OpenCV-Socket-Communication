import socket

host = ''
port = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host, port))

data= s.recvfrom(1024)[0].decode()
print(data)

s.close()


