import cv2
import random


img=cv2.imread('girl.jpg',0)
height,width=img.shape
print(height,width)

for i in range(0,height,3):
    h=random.randint(0,height)
    r1=random.randint(1,10)
    #for j in range(width):
    for k in range(r1):
        r2=random.randint(0,width-1)
        img[h,r2]=random.randint(0,255)
        

cv2.imwrite('noisy_picture.jpg',img)
cv2.waitKey()            