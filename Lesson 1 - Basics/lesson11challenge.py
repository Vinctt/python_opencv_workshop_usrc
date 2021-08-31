
import cv2

img = cv2.imread('..\Photos\question.jpg')
cv2.imshow('Original',img)

def rescale_frame(frame,scale=0.5):
    #works for images, video and live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv2.resize(frame,dimensions,interpolation =cv2.INTER_AREA)
#Rescaled
cv2.imshow('Rescaled',rescale_frame(img))
#Canny
canny=cv2.Canny(img,125,200)
cv2.imshow('Canny',canny)
#Blur
blur=cv2.GaussianBlur(img,(9,9),cv2.BORDER_DEFAULT)
#ksize has to be odd numbers
cv2.imshow('Blur',blur)
#Greyscale
greyscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey',greyscale)
#Circle
cv2.circle(img,(500,300),30,(200,0,0),thickness=2)
cv2.imshow('Circle', img)

cv2.waitKey(0)

while True:
    #20 is the delay
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
cv2.destroyAllWindows()