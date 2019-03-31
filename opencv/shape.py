import cv2 as cv
import numpy as np
import time

video = cv.VideoCapture(0)

while True:
    check, frame = video.read()
    blur = cv.GaussianBlur(frame, (21,21), 0)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    lower_green = np.array([30,86,0])
    upper_green = np.array([121,255,255])

    mask = cv.inRange(hsv, lower_green, upper_green)
    moments = cv.moments(mask)

    contoursArr = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    contours = contoursArr[0]

    contour_sizes = [(cv.contourArea(contour), contour) for contour in contours]
    biggest_contours = max(contour_sizes, key=lambda x: x[0])[1]
    
    x, y, w, h = cv.boundingRect(biggest_contours)
    cv.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
    cv.drawContours(frame, biggest_contours, -1, (0, 255, 0), 3)
    
    
    cv.imshow("capture", frame)
    cv.imshow("hsv", hsv)
    cv.imshow("mask", mask)

    key = cv.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv.destroyAllWindows

