import cv2 as cv

video = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')

out = cv.VideoWriter('output.avi', fourcc, 10.0, (640, 480))

while True:
    check, frame = video.read()

    if check == True:
        out.write(frame)
        cv.imshow('frame', frame)

        key = cv.waitKey(1)
        
        if key == ord('q'):
            break
    else:
        break

out.release()
video.release()
cv.destroyAllWindows
