import cv2 as cv
import numpy as np

cap = cv.VideoCapture('output.avi')

while cap.isOpened():
    ret,frame = cap.read()

    cv.imshow('video',frame)

    if cv.waitKey(60) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()