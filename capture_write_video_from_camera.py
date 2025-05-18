import numpy
import cv2

cap = cv2.VideoCapture(0)
# for save video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        # write the flipped frame
        out.write(frame)
        cv2.imshow("webcam",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()