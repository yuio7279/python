import cv2

img = cv2.imread('./pi_0525/photo.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('./pi_0525/haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for(x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x +w,y +h),(255,0,0),2)

cv2.imshow('photo',img)
cv2.waitKey(0)
cv2.destroyAllWindows()