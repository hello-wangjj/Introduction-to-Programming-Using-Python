import cv2
import numpy as np

__author__ = 'wangj'
__date__ = '2017/12/29 01:02'


def draw_flow(next_gray, flow, step=8):
    h, w = next_gray.shape[:2]
    # 以网格的形式选取二维图像上等间隔的点，这里间隔为16，reshape成2行的array
    y, x = np.mgrid[step / 2:h:step, step / 2:w:step].reshape(2, -1).astype(int)
    # 取选定网格点坐标对应的光流位移
    fx, fy = flow[y, x].T
    lines = np.vstack([x, y, x + fx, y + fy]).T.reshape(-1, 2, 2)  # 将初始点和变化的点堆叠成2*2的数组
    lines = np.int32(lines + 0.5)  # 忽略微小的假偏移，整数化
    vis = cv2.cvtColor(next_gray, cv2.COLOR_GRAY2BGR)
    cv2.polylines(vis, lines, 0, (0, 255, 0))  # 以初始点和终点划线表示光流运动
    for (x1, y1), (x2, y2) in lines:
        cv2.circle(vis, (x1, y1), 1, (0, 255, 0), -1)  # 在初始点（网格点处画圆点来表示初始点）
    cv2.imwrite('optik_flow.jpg', vis)
    return vis


def draw_hsv(flow):
    h, w = flow.shape[:2]
    fx, fy = flow[:, :, 0], flow[:, :, 1]
    ang = np.arctan2(fy, fx) + np.pi
    v = np.sqrt(fx * fx + fy * fy)
    hsv = np.zeros((h, w, 3), np.uint8)
    hsv[..., 0] = ang * (180 / np.pi / 2)
    hsv[..., 1] = 255
    hsv[..., 2] = np.minimum(v * 4, 255)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return bgr


def wrap_flow(cur_glitch, flow):
    h, w = flow.shape[:2]
    flow = -flow
    flow[:, :, 0] += np.arange(w)
    flow[:, :, 1] += np.arange(h)[:, np.newaxis]
    res = cv2.remap(cur_glitch, flow, None, cv2.INTER_LINEAR)
    print(flow.shape)
    return res


if __name__ == '__main__':
    start_img = cv2.imread('images/SmallVortices_001.bmp')
    later_img = cv2.imread('images/SmallVortices_002.bmp')
    print(type(start_img))
    cv2.namedWindow('start_img')
    cv2.imshow('start_img', start_img)
    cv2.namedWindow('later_img')
    cv2.imshow('later_img', later_img)

    prev_gray = cv2.cvtColor(start_img, cv2.COLOR_BGR2GRAY)

    show_hsv = False
    show_glitch = False
    cur_glitch = start_img.copy()

    next_gray = cv2.cvtColor(later_img, cv2.COLOR_BGR2GRAY)

    # Farnback 光流法
    flow = cv2.calcOpticalFlowFarneback(prev_gray, next_gray, None, 0.3, 2, 15, 3, 5, 1.2, 0)

    cv2.imshow('flow', draw_flow(next_gray, flow))

    show_hsv = not show_hsv
    print('HSV flow visualization is', ['off', 'on'][show_hsv])
    if show_hsv:
        cv2.imshow('flow HSV', draw_hsv(flow))

    show_glitch = not show_glitch
    if show_glitch:
        cur_glitch = later_img.copy()
        cur_glitch = wrap_flow(cur_glitch, flow)
        cv2.imwrite('glitch.jpg', cur_glitch)
    print('glitch is', ['off', 'on'][show_glitch])

    key = cv2.waitKey(5)

    if key == ord('q'):
        cv2.destroyAllWindows()

