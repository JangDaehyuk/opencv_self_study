"""color video Histogram"""

import cv2
import matplotlib.pyplot as plt

src = cv2.imread('lenna_2.jpg')

colors = ['b', 'g', 'r']

bgr_plans = cv2.split(src)

for (p, c) in zip(bgr_plans, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

cv2.imshow('src', src)
cv2.moveWindow('src', 900, 200)

cv2.waitKey(1)

plt.show()
