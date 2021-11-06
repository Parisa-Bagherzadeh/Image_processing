import cv2
import numpy as np
img=np.ones([250,250])
height,width=img.shape

print(height,width)

img[35:210,25:50]=0
img[35:55,50:115]=0
img[56:96,116:136]=0
img[97:117,50:115]=0
cv2.imshow('Image',img)
cv2.imwrite('result2.jpg',255*img)
cv2.waitKey()

