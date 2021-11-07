import cv2
import numpy as np
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(10, 7))
images1=[]
images2=[]
images3=[]
images4=[]
for i in range(1,6):
    img=cv2.imread(f'{i}.jpg',0)
    images1.append(img)
    rows,cols=img.shape

result1=np.zeros((rows,cols),dtype='uint8')

for image in images1:
    result1+=image//5

cv2.imwrite('Image1.jpg',result1)

for i in range(6,11):
    img=cv2.imread(f'{i}.jpg',0)
    images2.append(img)
    rows,cols=img.shape

result2=np.zeros((rows,cols),dtype='uint8')

for image in images2:
    result2+=image//5

cv2.imwrite('Image2.jpg',result2)


for i in range(11,16):
    img=cv2.imread(f'{i}.jpg',0)
    images3.append(img)
    rows,cols=img.shape

result3=np.zeros((rows,cols),dtype='uint8')

for image in images3:
    result3+=image//5

cv2.imwrite('Image3.jpg',result3)


for i in range(16,21):
    img=cv2.imread(f'{i}.jpg',0)
    images4.append(img)
    rows,cols=img.shape

result4=np.zeros((rows,cols),dtype='uint8')

for image in images4:
    result4+=image//5

cv2.imwrite('Image4.jpg',result4)

img1=cv2.imread('Image1.jpg',0)
img2=cv2.imread('Image2.jpg',0)
img3=cv2.imread('Image3.jpg',0)
img4=cv2.imread('Image4.jpg',0)

x1,y1=img1.shape
x2,y2=img2.shape
x3,y3=img3.shape
x4,y4=img4.shape

imgh1=cv2.hconcat([img1,img2])
imgh2=cv2.hconcat([img3,img4])
imgv=cv2.vconcat([imgh1,imgh2])
cv2.imwrite('Result.jpg',imgv)
cv2.waitKey()