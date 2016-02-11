import cv2 as cv
import numpy as np
import time

video = cv.VideoCapture(0)

ptsX = list()
ptsY = list()

blueLow = np.array([30,86,40])
blueUpp = np.array([121,255,255])

blueLow = np.array([40, 86, 30])
blueUpp = np.array([255, 255, 121])

while True:
    check, frame = video.read()
    blur = cv.GaussianBlur(frame, (11,11), 0)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
    
    

    mask = cv.inRange(hsv, blueLow, blueUpp)
    mask = cv.erode(mask, None, iterations = 2)
    mask = cv.dilate(mask, None, iterations = 2)    
    
    moments = cv.moments(mask)

    contArr = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = contArr[0]

    if len(contours) > 0:
        contMax = max(contours, key = cv.contourArea)
        ((x,y), radius) = cv.minEnclosingCircle(contMax)
        M = cv.moments(contMax)
        x = int(M["m10"] / M["m00"])
        y = int(M["m01"] / M["m00"])

        if radius > 20:
            cv.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            ptsX.append(x)
            ptsY.append(y)

    #contour_sizes = [(cv.contourArea(contour), contour) for contour in contours]
    #biggest_contours = max(contour_sizes, key=lambda x: x[0])[1]
    
    #x, y, w, h = cv.boundingRect(biggest_contours)
    #cv.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
    #cv.drawContours(frame, biggest_contours, -1, (0, 255, 0), 3)

    for i in range(1, len(ptsX)):
        cv.line(frame, (ptsX[i - 1], ptsY[i - 1]), (ptsX[i], ptsY[i]), (0, 0, 255), 5)

    cv.imshow("capture", frame)
    cv.imshow("hsv", hsv)
    cv.imshow("mask", mask)

    key = cv.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv.destroyAllWindows

