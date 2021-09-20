import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('../Faces/usrc_all.png')
#cv2.imshow('Lady',img)

#convert to greyscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Lady',gray)
frame = cv2.imread('../Faces/imageframe.png')
frame = cv2.resize(frame,(200,200))
#store the haar face database to haarCascade
haarCascade=cv2.CascadeClassifier('haar_face.xml')

#detect a face and return the rectangular coordinates of the face
facesRect=haarCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=13)
#modify minNeighbors to help filter noise

print(f'Number of faces found = {len(facesRect)}')

#get coordinates from facesRect and draw rectangles
i = 0
for (x,y,w,h) in facesRect:
    i += 1
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    cropped = img[y:y+h, x:x+w]
    cropped = cv2.resize(cropped,(160,160))
    frame[20:180,20:180] = cropped
    cv2.imwrite("Framed"+str(i)+".png", frame)

cv2.imshow('framed',frame)

cv2.waitKey(0)