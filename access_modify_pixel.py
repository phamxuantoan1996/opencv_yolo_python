import cv2 as cv
import numpy as np

image = cv.imread("nap_chai.jpg",cv.IMREAD_COLOR_BGR)

# read shape
# print('shape : ',image.shape)

# read size
# print('size : ',image.size)

# read size
# print('type : ',image.dtype)

roi_image = image[100:200,100:200]
image[100:200,100:200] = 0

cv.imshow('image',image)
cv.waitKey(0)
cv.destroyAllWindows()