import cv2 as cv
import numpy as np
import serial

#ser = serial.Serial('/dev/ttyUSB0', 115200)

#ser.write(str(data.data))

def find_if_close(cnt1,cnt2):
    row1,row2 = cnt1.shape[0],cnt2.shape[0]
    for i in xrange(row1):
        for j in xrange(row2):
            dist = np.linalg.norm(cnt1[i]-cnt2[j])
            if abs(dist) < 50 :
                return True
            elif i==row1-1 and j==row2-1:
                return False

video = cv.VideoCapture(0)

check, frame = video.read()
gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
firstFrame = cv.GaussianBlur(gray, (21, 21), 0)

while True:

	check, frame = video.read()
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	gray = cv.GaussianBlur(gray, (21, 21), 0)

	delFrame = cv.absdiff(firstFrame, gray)
	
	_,thresh = cv.threshold(gray,127,255,0)
	_,contours,_ = cv.findContours(thresh,cv.RETR_EXTERNAL,2)

	LENGTH = len(contours)
	status = np.zeros((LENGTH,1))	#1D array of len cnts.size() with all zeros

	for i,cnt1 in enumerate(contours):
	    x = i    
	    if i != LENGTH-1:
		for j,cnt2 in enumerate(contours[i+1:]):
		    x = x+1
		    dist = find_if_close(cnt1,cnt2)
		    if dist == True:
		        val = min(status[i],status[x])
		        status[x] = status[i] = val
		    else:
		        if status[x]==status[i]:
		            status[x] = i+1

	unified = []
	maximum = int(status.max())+1
	for i in xrange(maximum):
	    pos = np.where(status==i)[0]
	    if pos.size != 0:
		cont = np.vstack(contours[i] for i in pos)
		hull = cv.convexHull(cont)
		unified.append(hull)

	cv.drawContours(frame,unified,-1,(0,255,0),2)
	cv.drawContours(thresh,unified,-1,255,-1)

	cv.imshow("image", frame)
	cv.imshow("delFrame", delFrame)
	cv.imshow("thresh", thresh)
	
	key = cv.waitKey(1)

	if key == ord('q'):
		break
	
video.release()
cv.destroyAllWindows
