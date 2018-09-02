from OpenCVSockets import OpenCVServerSocket as SS
import cv2

server = SS(12345)

frame = server.receiveFrame()
cv2.imshow("Frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
