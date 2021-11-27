import cv2
import numpy as np

img_flower_input=cv2.imread('flower_input.jpg')
img_flower_input=cv2.cvtColor(img_flower_input,cv2.COLOR_BGR2GRAY)
mask=np.ones((25,25))/625.0
result=np.zeros((img_flower_input.shape))

rows,cols=img_flower_input.shape

for i in range(12,rows-12):
    for j in range(12,cols-12):
        small_img=img_flower_input[i-12:i+13,j-12:j+13]
        if np.all(small_img[0:11,0:11]>=0) and np.all(small_img[0:11,0:11]<=150):
           img_flower_input[i,j]=np.sum(small_img*mask)
result=img_flower_input
cv2.imwrite('flower.jpg',result)


