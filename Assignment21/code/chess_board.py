import cv2
import numpy as np
img=np.ones([320,320])
height,width=img.shape
for r in range(0,20,1):
    if r%2==1:
       for i in range(0,height,80):
           for j in range(0,width,80):
               img[i:i+40,j:j+40]=0

    elif r%2==0:
        for i in range(40,height,80):
            for j in range(40,width,80):
                img[i:i+40,j:j+40]=0
         
cv2.imwrite('chessboard.jpg',255*img)
cv2.imshow('image',img)
cv2.waitKey()