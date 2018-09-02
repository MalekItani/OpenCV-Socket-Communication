import socket
import numpy as np
from _pickle import loads
import cv2
import imutils
import struct

host = ''
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(5)

conn, addr = s.accept()


try:
    data = b""
    payload_size = struct.calcsize(">L")
    while len(data) < payload_size:
        print("Recv: {}".format(len(data)))
        data += conn.recv(4096)
        conn.send("Server received array of shape {0}".format(len(data)).encode())
        imgSize = struct.unpack('>L', data[:payload_size])[0]
        data = data[payload_size:]
        while len(data) < imgSize:
            data += conn.recv(4096)
    
    frame_data = data[:imgSize]
    data = data[imgSize:]

    frame=loads(frame_data, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
#        img = imutils.resize(data, 600)
#        img = cv2.medianBlur(img, 11)
    cv2.imwrite('Res.jpg', frame)
    print(data)
except Exception as inst:
    print(type(inst))
    print(inst)
    conn.close()
    s.close()


