import cv2
import numpy as np

__author__ = 'wangj'
__date__ = '2017/11/01 23:39'

# 当鼠标按下时为True
drawing = False
# 如果mode为true时绘制矩形，按下'm'变成绘制曲线
mode = True
ix, iy = -1, -1


def main():
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print(events, sep='\n')


# mouse callback function

# def draw_circle(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


# 创建回调函数
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    # 当按下左键时返回起始位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    # 当左键按下并移动时绘制图形，event可以查看移动，flag查看是否按下
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                # 绘制圆圈，小圆点连在一起就成了线，3代表笔画的粗细
                cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

    # 当鼠标松开时停止绘图
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False


if __name__ == '__main__':
    # main()
    # 创建图像与窗口并将窗口与回调函数绑定
    # img = np.zeros((500, 500, 3), np.uint8)
    # cv2.namedWindow('image')
    # cv2.setMouseCallback('image', draw_circle)
    #
    # while (1):
    #     cv2.imshow('image', img)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q键退出
    #         break
    # cv2.destroyAllWindows()
    img = np.zeros((500, 500, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)
    while (1):
        cv2.imshow('image', img)
        k = cv2.waitKey(1)
        if k == ord('m'):
            mode = not mode
        elif k == ord('q'):
            break
    cv2.destroyAllWindows()
