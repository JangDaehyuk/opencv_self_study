# R,G,B 가 모두 있는 트랙바

import numpy as np
import cv2


def nothing(x):
    pass


frame = np.zeros((512, 512, 3), np.uint8)
cv2. namedWindow('frame')

cv2.createTrackbar('R', 'frame', 0, 255, nothing)
cv2.createTrackbar('G', 'frame', 0, 255, nothing)
cv2.createTrackbar('B', 'frame', 0, 255, nothing)

while True:
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

    r = cv2.getTrackbarPos('R', 'frame')
    g = cv2.getTrackbarPos('G', 'frame')
    b = cv2.getTrackbarPos('B', 'frame')

    frame[:] = [b, g, r]

cv2.destroyAllWindows()
