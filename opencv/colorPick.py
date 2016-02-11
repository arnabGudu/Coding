import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

while True:
    check, frame = video.read()
    color = np.uint8([[[255,0,0]]])
    hsv_color = cv.cvtColor(color, cv.COLOR_BGR2HSV)
    print(hsv_color)
    #cv.line(frame, (0,0), (100,100), hsv_color, 10)

    cv.imshow('frame', frame)
    key = cv.waitKey(1)
    if (key == ord('q')):
        break
video.release()
cv.destroyAllWindows

