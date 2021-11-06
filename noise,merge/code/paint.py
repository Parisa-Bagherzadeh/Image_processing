import cv2

img=cv2.imread('nature.jpg',0)
inverted=255-img
blurred=cv2.GaussianBlur(inverted,(21,21),0)
inverted_blurred=255-blurred
sketch=img/inverted_blurred
sketch=sketch*230
cv2.imwrite('paint.jpg',sketch)