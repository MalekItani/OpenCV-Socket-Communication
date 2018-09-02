import socket

host = ''
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

conn, addr = s.accept()

size = int(conn.recv(1))
print('Preparing to receive an array of size: {0}'.format(size)) 

data = []
for i in range(size):
    data.append(int(conn.recv(1)))
print(data)
conn.send('SUCCESS'.encode())
conn.close()
s.close()


