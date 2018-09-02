import socket
import numpy as np
from _pickle import dumps
import cv2
import imutils
import time

# Initializing numpy payload
shape = (10,10, 3)
data = np.random.randint(0, 10, shape)
img = cv2.imread('Mario.jpg')#, cv2.IMREAD_GRAYSCALE)
img = imutils.resize(img, 50)
print("Payload is: ")
print(img)
# Local machine host & chosen port. For remote connections over wifi change the domain to the IP of the remote server.
# host = '127.0.0.1'
host = '192.168.2.211'
port = 12345 

# Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((host, port))

t1 = time.time()
s.send(dumps(img))
response = s.recv(1024)
print("Receive the following response: " + response.decode())
t2 = time.time()

print("Time taken: {0}".format(t2 - t1))

s.close()

