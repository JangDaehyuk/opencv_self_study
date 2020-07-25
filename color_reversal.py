import os

import cv2

path = os.path.join('my_images', '고양이.jpg')
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

img2 = ~img  # not 연산자를 하면 색을 반전시킬 수 있다. 어두운 부분은 밝게, 밝은 부분은 어둡게 된다.

cv2.namedWindow('image1', cv2.WINDOW_NORMAL)
cv2.imshow('image1', img)
cv2.moveWindow('image1', 200, 200)
cv2.resizeWindow('iamge1', 700, 900)


cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
cv2.imshow('image2', img2)
cv2.moveWindow('image2', 600, 200)
cv2.resizeWindow('iamge2', 700, 900)

cv2.waitKey()
cv2.destroyAllWindows()
