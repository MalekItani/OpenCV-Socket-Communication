from OpenCVSockets import OpenCVClientSocket as CS
import cv2

client = CS('127.0.0.1',12345)

img = cv2.imread('Mario.jpg')
client.sendFrame(img)


