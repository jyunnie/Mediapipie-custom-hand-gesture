import cv2
import sys

cameraId = 0
delay = 1
window_name = 'realtime'

cam = cv2.VideoCapture(cameraId)

if not cam.isOpened():
	sys.exit()

while True:
	ret, frame = cam.read()
	cv2.imshow(window_name, frame)
	if cv2.waitKey(delay) & 0xFF == ord('q'):
		break

cv2.destroyWindow(window_name)
