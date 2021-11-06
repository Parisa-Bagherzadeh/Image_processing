import cv2
img1=cv2.imread('a.tif',0)
img2=cv2.imread('b.tif',0)

img3=img2-img1
cv2.imwrite('result2.jpg',img3)
cv2.imshow('image',img3)
cv2.waitKey()