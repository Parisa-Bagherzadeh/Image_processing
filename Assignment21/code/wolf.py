import cv2
import numpy as np

img=cv2.imread('4.jpg',0)

height,width=img.shape
for i in range(height):
    for j in range(width):
        if img[i,j]<=130:
            img[i,j]=0
cv2.imwrite('result6.jpg',img)
cv2.waitKey()
        



          

