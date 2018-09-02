import socket
import numpy as np
from _pickle import loads, dumps
import cv2
import imutils


class OpenCVServerSocket:
    def __init__(self, port):
        self.host = ''
        self.port = port
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Socket.bind((self.host, self.port))
        self.Socket.listen(1)
        self.clientConn, self.clientAddr = self.Socket.accept()

    def receiveFrame(self):
        data = np.array(loads(self.clientConn.recv(16384)))
        self.clientConn.send("Server received array of shape {0}".format(data.shape).encode())
        return data


class OpenCVClientSocket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Socket.connect((host, port))
        self.clientConn, self.clientAddr = self.Socket.accept()

    def sendFrame(self, frame):
        self.Socket.send(dumps(frame))
