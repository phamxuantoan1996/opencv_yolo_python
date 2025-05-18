import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)

# draw line
# cv.line(img,(0,0),(511,511),(255,0,0),5)

# draw rectangle
# cv.rectangle(img,(100,100),(200,200),(255,0,0),1)

# draw circle
# cv.circle(img,(256,256),100,(255,0,0),1)

# draw ellipse
# cv.ellipse(img,(256,256),(100,50),45,0,360,(255,0,0),1)

# adding text
cv.putText(img,'OpenCV',(100,100),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv.LINE_AA)

cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()