import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(20,30),(255,255,255),5)
cv2.rectangle(img,(50,25),(100,50),(0,0,255),5)
cv2.circle(img,(44,64), 20, (0,255,0), -1)
pts = np.array([[10,50],[20,30],[70,200],[50,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(10,50), font, 1, (200,255,155), 1, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()