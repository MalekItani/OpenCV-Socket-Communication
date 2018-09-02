import socket
import numpy as np
from _pickle import loads
import cv2
import imutils

host = ''
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(5)

conn, addr = s.accept()


try:
    while(True):
        data = np.array(loads(conn.recv(16384)))
        conn.send("Server received array of shape {0}".format(data.shape).encode())
        img = imutils.resize(data, 600)
        img = cv2.medianBlur(img, 11)
        cv2.imwrite('Res.jpg', img)
        print(data)
except Exception as inst:
    print(type(inst))
    print(inst)
    conn.close()
    s.close()


