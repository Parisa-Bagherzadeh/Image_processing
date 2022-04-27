import cv2
import numpy as np
img=np.ones([800,800])
height,width=img.shape
for r in range(0,20,1):
    if r%2==1:
       for i in range(0,height,200):
           for j in range(0,width,200):
               img[i:i+100,j:j+100]=0

    elif r%2==0:
        for i in range(100,height,200):
            for j in range(100,width,200):
                img[i:i+100,j:j+100]=0
         
cv2.imwrite('chessboard.jpg',255*img)
cv2.imshow('chessboard',img)
cv2.waitKey()