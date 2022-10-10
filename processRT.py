import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #threshold 1 is binary inverted
    _,thres = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)
    dst = cv2.addWeighted(gray, 0.7, thres, 0.3,0)
    #color = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    # Display the resulting frame
    cv2.imshow('frame',thres)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()