import cv2

img=cv2.imread('paris.jpg',0)

height,width=img.shape
print(height,width)

item=120
for i in range(145):
    for j in range(100-i,145-i):
        if(j>=0):
          img[i,j]=0
 


      

cv2.imshow('Paris',img)
cv2.imwrite('Paris.jpg',img)
cv2.waitKey()