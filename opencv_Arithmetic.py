import os

import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

path = os.path.join('my_images', '고양이.jpg')
src1 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

h, w = src1.shape
print(h, w)

src2 = np.ones((h, w), dtype=np.uint8)
cv2.rectangle(src2, (50, 50), (200, 200), 255, -1)

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)
dst2 = cv2.subtract(src1, src2, dtype=cv2.CV_8U)
dst3 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)
dst4 = cv2.absdiff(src1, src2)

fig = plt.figure(figsize=(15, 6))
gs = gridspec.GridSpec(nrows=3,  # row 몇 개
                       ncols=2,  # col 몇 개
                       height_ratios=[2, 2, 2],
                       width_ratios=[3, 3]
                       )

plt.subplot(231), plt.axis('off'), plt.imshow(
    src1, cmap='gray'), plt.title('src1')
plt.subplot(232), plt.axis('off'), plt.imshow(
    src2, cmap='gray'), plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(
    dst1, cmap='gray'), plt.title('dst1')
plt.subplot(234), plt.axis('off'), plt.imshow(
    dst2, cmap='gray'), plt.title('dst2')
plt.subplot(235), plt.axis('off'), plt.imshow(
    dst3, cmap='gray'), plt.title('dst3')
plt.subplot(236), plt.axis('off'), plt.imshow(
    dst4, cmap='gray'), plt.title('dst4')

plt.show()
