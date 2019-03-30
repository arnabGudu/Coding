import cv2
img = cv2.imread ("img.png", 1)
cv2.imshow("img", img)
cv2.waitKey(2000)

#resize square
resized = cv2.resize(img, (600,600))
cv2.imshow("img", resized)
cv2.waitKey(2000)

#resize reduce
resized = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
cv2.imshow("img", resized)
cv2.waitKey(2000)

#resize enlarge
resized = cv2.resize(img, (int(img.shape[1] * 2), int(img.shape[0] * 2)))
cv2.imshow("img", resized)
cv2.waitKey(2000)

cv2.destroyAllWindows()
