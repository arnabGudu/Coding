import cv2 as cv
import numpy as np


video = cv.VideoCapture(0)

ptsX = [[],[]]  #2D lists
ptsY = [[],[]]

#blueLow = np.array([100,50,50])
#blueUpp = np.array([120,255,255])

#redLow = np.array([0, 100, 100])
#redUpp = np.array([5, 255, 255])


#threshold values for red and blue objects
lower = [np.array([0, 100, 100]), np.array([100,50,50])]
upper = [np.array([5, 255, 255]), np.array([120,255,255])]



while True:

    check, frame = video.read()
    
    blur = cv.GaussianBlur(frame, (11,11), 0)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)       

    #when i = 0 red will be tracked and when i = 1 blue will be tracked
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

            l = len(ptsX[i])
	    
            for j in range(1, l):
                
                thickness = int((j * 5) / l)        #thickness reduces as points increases

                color = [(0, 0, 255), (255, 0, 0)]
                
                #trace only when thickness is > 1, this is for the fading effect
                if thickness > 1:
                    cv.line(frame, (ptsX[i][j - 1], ptsY[i][j - 1]), (ptsX[i][j], ptsY[i][j]), color[i], thickness)
	
        cv.imshow("capture", frame)
    	#cv.imshow("hsv", hsv)

    key = cv.waitKey(1)
    
    if key == ord('q'):     #press q to quit
        break

video.release()
cv.destroyAllWindows

