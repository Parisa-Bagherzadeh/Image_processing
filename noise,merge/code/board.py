import cv2

test=cv2.imread('test.bmp',0)
origin=cv2.imread('origin.bmp',0)

result=cv2.subtract(test,origin)

cv2.imwrite('board.jpg',result)
