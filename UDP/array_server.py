import socket

host = ''
port = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host, port))

si, addr = s.recvfrom(1)

size = int(si)
print('Preparing to receive an array of size: {0}'.format(size))

data = []
for i in range(size):
    data.append(int(s.recvfrom(1)[0]))

print(data)
s.sendto("SUCCESS".encode(), addr)
s.close()


