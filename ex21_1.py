import cv2
import numpy as np
img=np.ones([255,255],dtype=np.uint8)
height,width=img.shape

print('height=',height,'width=',width)
for i in range(height):
    for j in range(width):
        img[i,j]=255-i
cv2.imshow('Image',img)
cv2.imwrite('result1.jpg',img)
cv2.waitKey()