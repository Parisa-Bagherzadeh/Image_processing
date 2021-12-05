import cv2

image=cv2.imread('low_contrast.jpg',0)
high_contrast_image=cv2.normalize(image,image,0,255,cv2.NORM_MINMAX)
cv2.imshow('image',image)
cv2.imshow('image',image)
cv2.imwrite('high_contast.jpg',high_contrast_image)
cv2.waitKey(0)