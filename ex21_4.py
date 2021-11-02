import cv2
img1=cv2.imread('1.jpg',0)
img2=cv2.imread('2.jpg',0)
img1=255-img1
img2=255-img2

cv2.imshow('Image1',img1)
cv2.imshow('Image2',img2)
cv2.imwrite('female.jpg',img1)
cv2.imwrite('male.jpg',img2)
cv2.waitKey()
