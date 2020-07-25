'''영상을 마우스로 드레그한 영역을 grayscale 로 변환하여 새로운 윈도우에 띄우는 프로그램 개발'''

import os

import cv2


# 마우스 왼쪽 버튼 상태 체크를 위한 변수
mouse_is_pressing = False
# 최초로 마우스 왼쪽 버튼 누른 위치를 저장하기 위해 사용
start_x, start_y = -1, -1


def mouse_callback(event, x, y, flags, param):
    global mouse_is_pressing, start_x, start_y

    img_result = img_color.copy()

    # 마우스 왼쪽 버튼 누를 시 발생 이벤트
    if event == cv2.EVENT_LBUTTONDOWN:

        mouse_is_pressing = True
        start_x, start_y = x, y
        cv2.circle(img_result, (x, y), 10, (0, 0, 255), -1)
        cv2.imshow('img_color', img_result)

    # 마우스 이동시 발생하는 이벤트
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_is_pressing:
            # 마우스 이동하는 조건인 true 동안 rectangle 그리기
            cv2.rectangle(img_result, (start_x, start_y),
                          (x, y), (0, 0, 255), -1)
            cv2.imshow('img_color', img_result)

    # 마우스 왼쪽 버튼에서 손을 떼면 발생하는 이벤트
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_is_pressing = False

        # img_cat = img_color[start_y:y, start_x:x] # 왼쪽에서 오른쪽 아래로만 드래그가 되는 상태.

        # min, max가 들어가는 이유는 클릭을 한 뒤에 마우스의 이동방향이 상하좌우 아무 방향으로든 향할 수 있다. 이 때, grayscale 이 적용되는 일부 픽셀을 선택하고 추출해서 변수화.

        img_cat = img_color[min(start_y, y):max(
            start_y, y), min(start_x, x): max(start_x, x)]
        img_cat = cv2.cvtColor(img_cat, cv2.COLOR_BGR2GRAY)
        img_cat = cv2.cvtColor(img_cat, cv2.COLOR_GRAY2BGR)

        img_result[min(start_y, y):max(start_y, y), min(
            start_x, x): max(start_x, x)] = img_cat

        # 그림에 대한 세가지 객체가 존재합니다. img_color(원본), img_result(원본에서 일부 픽셀에 grayscale 적용되어 변한 사본), img_cat (gray scale 적용된 일부 픽셀)
        # cv2.imshow('img_result', img_result)
        cv2.imshow('img_color', img_result)
        cv2.imshow('img_cat', img_cat)


path = os.path.join('my_images', '고양이.jpg')
img_color = cv2.imread(path)

# img_color = cv2.imread('apple.jpg')

# 최초의 영상
cv2.imshow('img_color', img_color)

cv2.setMouseCallback('img_color', mouse_callback)

cv2.waitKey()
cv2.destroyAllWindows()
