import cv2
import numpy as np
import matplotlib.pyplot as plt

src1 = cv2.imread('lenna.jpg', cv2.IMREAD_GRAYSCALE)
h, w = src1.shape
src2 = np.ones((h, w), dtype=np.uint8)

# src2 를 흑백 절반으로 바꾸기 
for x in range(int(w/2)):
    for y in range(h):
        src2[y, x] = 255  

cv2.imshow('src1', src1)
cv2.imshow('src2', src2)

bit_and = cv2.bitwise_and(src1, src2)
bit_or = cv2.bitwise_or(src1, src2)
bit_not = cv2.bitwise_not(src1, src2)
bit_xor = cv2.bitwise_xor(src1, src2)

plt.subplot(221), plt.axis('off'), plt.imshow(
    bit_and, cmap='gray'), plt.title('blt_and')
plt.subplot(222), plt.axis('off'), plt.imshow(
    bit_or, cmap='gray'), plt.title('bit_or')
plt.subplot(223), plt.axis('off'), plt.imshow(
    bit_not, cmap='gray'), plt.title('bit_not')
plt.subplot(224), plt.axis('off'), plt.imshow(
    bit_xor, cmap='gray'), plt.title('bit_xor')

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
