import cv2

img = cv2.imread('..\Photos\question.jpg')
cv2.imshow('Cat', img)


while True:

#     #if the d key is pressed, kill screen
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

cv2.destroyAllWindows()