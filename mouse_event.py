import cv2 as cv
import numpy as np

def mouse_callback(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        print('coordinate : x = ',x,' , y = ',y)

cv.namedWindow('image')
cv.setMouseCallback('image',mouse_callback)
while True:
    image = np.zeros((512,512,3),np.uint8)
    cv.imshow('image',image)
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()