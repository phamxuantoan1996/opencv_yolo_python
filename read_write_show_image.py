import cv2 as cv
import numpy as np

img = cv.imread(filename='nap_chai.jpg',flags=cv.IMREAD_COLOR)
cv.imwrite("nap_chai_copy.jpg",img)

cv.imshow('image',img)
cv.waitKey(delay=0)
cv.destroyAllWindows()