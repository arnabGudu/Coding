#face detection
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

gray_img = cv2.imread("face.jpg")

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
