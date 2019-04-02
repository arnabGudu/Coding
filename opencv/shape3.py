import cv2 as cv
import numpy as np
import time

video = cv.VideoCapture(0)

ptsX = [[],[]]
ptsY = [[],[]]

#blueLow = np.array([100,50,50])
#blueUpp = np.array([120,255,255])

#redLow = np.array([0, 100, 100])
#redUpp = np.array([10, 255, 255])

lower = [np.array([0, 100, 100]), np.array([100,50,50])]
upper = [np.array([10, 255, 255]), np.array([120,255,255])]

while True:
    check, frame = video.read()
    blur = cv.GaussianBlur(frame, (11,11), 0)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)    

    for i in range(0, 2):
        mask = cv.inRange(hsv, lower[i], upper[i])
	mask = cv.erode(mask, None, iterations = 2)
	mask = cv.dilate(mask, None, iterations = 2)

	contArr = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	contours = contArr[0]

	if len(contours) > 0:
            contMax = max(contours, key = cv.contourArea)
       	    ((x,y), radius) = cv.minEnclosingCircle(contMax)
	    M = cv.moments(contMax)
	    x = int(M["m10"] / M["m00"])
	    y = int(M["m01"] / M["m00"])

	    if radius > 20:
                color = [(0, 255, 255), (255, 255, 0)]
	        cv.circle(frame, (x, y), int(radius), color[i], 2)
	        ptsX[i].append(x)
	        ptsY[i].append(y)

	    for j in range(1, len(ptsX[i])):
                thickness = 5
                print (j + 5) / len(ptsX[i])
                color = [(0, 0, 255), (255, 0, 0)]
                cv.line(frame, (ptsX[i][j - 1], ptsY[i][j - 1]), (ptsX[i][j], ptsY[i][j]), color[i], thickness)
	
	cv.imshow("capture", frame)
    	#cv.imshow("hsv", hsv)
    	#cv.imshow("mask", mask)

    key = cv.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv.destroyAllWindows

