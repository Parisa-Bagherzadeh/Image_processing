import cv2
import numpy as np

img_building=cv2.imread('building.tif')
img_building=cv2.cvtColor(img_building,cv2.COLOR_BGR2GRAY)
vertical_filter=np.array([[-1,0,1],
               [-1,0,1],
               [-1,0,1]])


horizontal_filter=np.array([[-1,-1,-1],
                           [0,0,0],
                           [1,1,1]])

result_vertical=np.zeros(img_building.shape)

result_horizontal=np.zeros(img_building.shape)
rows,cols=img_building.shape

for i in range(1,rows-1):
    for j in range(1,cols-1):
        small_img=img_building[i-1:i+2,j-1:j+2]
        result_vertical[i,j]=np.sum(small_img*vertical_filter)
        result_horizontal[i,j]=np.sum(small_img*horizontal_filter)





#print(result)
cv2.imwrite('vertical_filter_building_output.jpg',result_vertical)
cv2.imwrite('horizontal_filter_building_output.jpg',result_horizontal)            
cv2.waitKey() 