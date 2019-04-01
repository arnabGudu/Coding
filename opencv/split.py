import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)
a = 0

while True:
    a = a + 1
    check, frame = video.read()
    blur = cv.GaussianBlur(frame, (21, 21), 0)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

    #blueLow = np.array([a,100,100])
    #blueUpp = np.array([a + 10,255,255])

    #print(a)

    #if (a >= 360):
    #    a = 0

    greenLow = np.array([50, 100, 100])
    greenUpp = np.array([70, 255, 255])

    redLow = np.array([0, 100, 100])
    redUpp = np.array([10, 255, 255])
    
    blueLow = np.array([100,100,100])
    blueUpp = np.array([120,255,255])

    maskGreen = cv.inRange(hsv, greenLow, greenUpp)
    maskBlue  = cv.inRange(hsv, blueLow, blueUpp)
    maskRed   = cv.inRange(hsv, redLow, redUpp)

    maskGreen = cv.erode(maskGreen, None, iterations = 2)
    maskBlue  = cv.erode(maskBlue,  None, iterations = 2)
    maskRed   = cv.erode(maskRed,   None, iterations = 2)

    maskGreen = cv.dilate(maskGreen, None, iterations = 2)
    maskBlue  = cv.dilate(maskBlue,  None, iterations = 2)
    maskRed   = cv.dilate(maskRed,   None, iterations = 2)


    #cv.imshow("frame", frame)
    cv.imshow("mGreen", maskGreen)
    cv.imshow("mBlue", maskBlue)
    cv.imshow("mRed", maskRed)
    #cv.imshow("hsv", hsv)


    key = cv.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv.destroyAllWindows
