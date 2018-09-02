import socket

host = ''
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(5)

conn, addr = s.accept()

data = conn.recv(1024).decode()
print(data)

conn.close()
s.close()


