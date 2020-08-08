import cv2
import numpy as np 

src = cv2.imread('lenna_2.jpg')

bgr_plans = cv2.split(src)

histSize = 256

histRange = (0,256)

accumulate = False

b_hist = cv2.calcHist(bgr_plans, [0], None, [histSize], histRange, accumulate=accumulate)
g_hist = cv2.calcHist(bgr_plans, [1], None, [histSize], histRange, accumulate=accumulate)
r_hist = cv2.calcHist(bgr_plans, [2], None, [histSize], histRange, accumulate=accumulate)

hist_w = 256*3
hist_h = 400
histImage = np.zeros((hist_h,hist_w,3), dtype=np.uint8)

cv2.normalize(b_hist,b_hist,alpha=0,beta=hist_h,norm_type=cv2.NORM_MINMAX)
cv2.normalize(g_hist,g_hist,alpha=0,beta=hist_h,norm_type=cv2.NORM_MINMAX)
cv2.normalize(r_hist,r_hist,alpha=0,beta=hist_h,norm_type=cv2.NORM_MINMAX)

for i in range(0,histSize):

    cv2.line(histImage,(i,hist_h-int(np.round(b_hist[i]))),
    (i,hist_h - 0), (255,0,0), thickness=2)

    cv2.line(histImage,(i+256,hist_h-int(np.round(g_hist[i-1]))),
    (i+256,hist_h - 0), (0,255,0), thickness=2)

    cv2.line(histImage,(i+256*2,hist_h-int(np.round(r_hist[i-1]))),
    (i+256*2,hist_h - 0), (0,0,255), thickness=2)

cv2.imshow('Source image', src)
cv2.imshow('HIstogram', histImage)
cv2.waitKey()

