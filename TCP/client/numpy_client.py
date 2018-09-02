import socket
import numpy as np
from _pickle import dumps
import cv2
import imutils
import time
import struct

# Initializing numpy payload
shape = (10,10, 3)
data = np.random.randint(0, 10, shape)
img = cv2.imread('Mario.jpg')#, cv2.IMREAD_GRAYSCALE)
img = imutils.resize(img, 600)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
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
result, frame = cv2.imencode('.jpg', img, encode_param)
payload = dumps(frame)
size = len(payload)
s.send(struct.pack('>L',size)+payload)
response = s.recv(1024)
print("Receive the following response: " + response.decode())
t2 = time.time()

print("Time taken: {0}".format(t2 - t1))

s.close()

