import cv2
#import numpy

#reading images
img = cv2.imread('..\Photos\question.jpg')
cv2.imshow('Cat', img)

# reading videos

capture = cv2.VideoCapture('..\Videos\cows.mp4')
# #VideoCapture(0) = Webcam input

# #capture=cv2.VideoCapture(0)

while True:
    isTrue,frame=capture.read()
    print(isTrue)
    cv2.imshow('',frame)

#     #if the d key is pressed, kill screen
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()


cv2.waitKey(0)
