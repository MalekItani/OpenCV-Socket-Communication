import socket
from _pickle import loads, dumps
import cv2
import struct

class OpenCVServerSocket:
    def __init__(self, port, chunkSize=4096):
        self.cs = chunkSize
        self.host = ''
        self.port = port
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Socket.bind((self.host, self.port))
        self.Socket.listen(1)
        self.clientConn, self.clientAddr = self.Socket.accept()

    def receiveFrame(self):
        data = b""
        payload_size = struct.calcsize(">L")
        while len(data) < payload_size:
            data += self.clientConn.recv(self.cs)
            imgSize = struct.unpack('>L', data[:payload_size])[0]
            data = data[payload_size:]
            while len(data) < imgSize:
                data += self.clientConn.recv(self.cs)
        frame_data = data[:imgSize]
        frame = loads(frame_data, fix_imports=True, encoding="bytes")
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        return frame


class OpenCVClientSocket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Socket.connect((self.host, self.port))

    def sendFrame(self, frame):
        result, frame = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        payload = dumps(frame)
        size = len(payload)
        self.Socket.send(struct.pack('>L', size) + payload)
