import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)


while True:
    check, frame = video.read() 
    cv.imshow("capture", frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv.destroyAllWindows

