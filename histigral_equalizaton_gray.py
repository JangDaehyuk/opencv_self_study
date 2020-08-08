# 원본 영상과 어두운 영상을 모두 histigral equalizaton 한 결과

import cv2
import matplotlib.pyplot as plt

src1 = cv2.imread(
    'histogram equalization1.png', cv2.IMREAD_GRAYSCALE)

src2 = cv2.imread(
    'histogram equalization2.png', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.equalizeHist(src1)
dst2 = cv2.equalizeHist(src2)

plt.subplot(221), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(222), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(223), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('Histogram Equalization 1')
plt.subplot(224), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('Histogram Equalization 2')

plt.show()
