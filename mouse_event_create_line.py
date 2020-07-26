# 마우스가 지나간 길을 따라 선을 그려주는 프로그램 _ 개량

import cv2
import numpy as np

oldx = oldy = -1


def mouse_fn(event, x, y, flags, param):
    global img, oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y  # 이전 좌표를 받기
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            # Line_aa 옵션 넣어주면 좀 더 부드럽게 그려진다.
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            cv2.imshow('img', img)
            # 마우스 커서 이동한 위치를 저장
            oldx, oldy = x, y  # 이동한 점을 다시 받아주기


# 도화지 만들기
img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_fn, img)

cv2.imshow('img', img)
