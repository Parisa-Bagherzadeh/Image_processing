import cv2 
import numpy as np

images=[]

for i in range(14):
    print(i)
    img=cv2.imread(f'h{i}.jpg',0)
    images.append(img)
    #$print(i)
    rows,cols=img.shape

result=np.zeros((rows,cols),dtype='uint8')

for image in images:
    result+=image//14

cv2.imwrite('highway.jpg',result)