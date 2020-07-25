import os

import cv2

path = os.path.join('my_images', '고양이.jpg')
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)



cv2.namedWindow('image1', cv2.WINDOW_NORMAL)
cv2.imshow('image1', img)
cv2.moveWindow('image1', 200, 200)
cv2.resizeWindow('iamge1', 700, 900)

while True:
    key = cv2.waitKey()

    if key == ord('q'):
        img = ~img # 
        cv2.imshow('image1', img)
        # cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
        # cv2.imshow('image2', img2)
        # cv2.moveWindow('image2', 600, 200)
        # cv2.resizeWindow('iamge2', 700, 900)
    elif key == 27:
        break

# cv2.waitKey()
cv2.destroyAllWindows()
