import cv2
import numpy as np

img=cv2.imread('3.jpg',0)
height,width=img.shape
d_img=np.zeros([height,width],dtype=np.uint8)

for i in range(height):
    for j in range(width):
        d_img[i,j]=img[height-i-1,width-j-1]
        d_img=d_img[0:height,0:width]

cv2.imshow('Image',d_img)
cv2.imwrite('result5.jpg',d_img)
cv2.waitKey()        
