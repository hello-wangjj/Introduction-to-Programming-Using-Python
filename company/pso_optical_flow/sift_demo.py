import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pyswarms as pso
import numpy as np
import pandas as pd
import cv2

__author__ = 'wangj'
__date__ = '2018/01/14 21:31'


def save_sift_feature(img):
    img = cv.imread(img)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 创建sift类
    sift = cv.xfeatures2d.SIFT_create()
    # 在图像中找到关键点
    kp = sift.detect(gray, None)
    img = cv.drawKeypoints(gray, kp, img)
    # 计算每个点的sift
    des = sift.compute(gray, kp)
    # des[0] 关键点的list,des[1] 特征向量的矩阵
    img = cv.drawKeypoints(gray, kp, img)
    return img, des


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


def cal_theta(a, b):
    """
    特征点初匹配. 由于每个 SIFT 特征描述子是 128 维的向量,
    高维数据间的相似性通常采用光谱角距离来度量.
    光谱角距离越小表示两个特征点越相似.
    记录光谱角距离最小的特征点对, 并根据最近邻和次近邻的光谱角距离之比剔除误匹配点.

    :param a:
    :param b:
    :return: 光谱角, theta
    """
    a_mul_b = a.T.dot(b)
    a_norm_norm_b = np.linalg.norm(a, 2) * np.linalg.norm(b, 2)
    cos_theta = a_mul_b / a_norm_norm_b
    return 1.0 / np.cos(cos_theta)


def cal_dis(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


if __name__ == '__main__':
    img = cv2.imread('images/SmallVortices_001.bmp')
    img001, des_001 = save_sift_feature('images/SmallVortices_001.bmp')
    img002, des_002 = save_sift_feature('images/SmallVortices_002.bmp')
    cv.imwrite('001.jpg', img001)
    cv.imwrite('002.jpg', img002)
    key_point_001 = des_001[0]
    key_point_feature_001 = des_001[1]
    key_point_002 = des_002[0]
    key_point_feature_002 = des_002[1]

    # Set-up hyperparameters
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

    # Call instance of PSO
    # 暂时用不上
    # optimizer = pso.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)

    # sift 特征是128维的向量
    # 遍历sift特征点,记录光谱角最小的特征对
    # all_theta = []
    # for ind, i in enumerate(key_point_feature_001):
    #     temp = []
    #     print(ind)
    #     for j in key_point_feature_002:
    #         theta = cal_theta(i,j)
    #         temp.append(theta)
    #     all_theta.append(temp)

    # 保存 theta 矩阵
    # print(np.array(all_theta))
    # np.savetxt('sift.txt', all_theta, fmt='%f', delimiter=',')
    # 导入 已保存的 sift 特征矩阵
    all_theta = np.loadtxt('sift.txt', delimiter=',')
    # print(all_theta.shape)  # 9059,6893
    # 记录最小值
    # arg = np.argmin(all_theta, axis=1)
    # 对应的特征点队
    # for i, j in enumerate(arg):
    #     p1_x, p1_y = np.int(key_point_001[i].pt[0]), np.int(key_point_001[i].pt[1])
    #     p2_x, p2_y = np.int(key_point_002[j].pt[0]), np.int(key_point_002[j].pt[1])
    #     cv2.line(img, (p1_x, p1_y), (p2_x, p2_y), (155, 155, 155))
    # # lines = np.vstack([x, y, x + fx, y + fy]).T.reshape(-1, 2, 2)  # 将初始点和变化的点堆叠成2*2的数组
    # cv2.imshow('11', img)
    # # 考虑取最小的100个值，比较距离，然后取最近的点
    # df_all_theta = pd.DataFrame(all_theta)
    # new_arg = np.array(df_all_theta.T.apply(np.argsort).T)[:, 0:100]
    # arg_list = new_arg.tolist()
    # args = []
    # for i, j in enumerate(arg_list):
    #     args.append(all_theta[i, j])
    # # 比较距离
    # inds = []
    # for i, arg in enumerate(args):
    #     temp = []
    #     for a in arg:
    #         distance = cal_dis(key_point_001[i].pt, key_point_002[int(a)].pt)
    #         temp.append(distance)
    #     temp = np.array(temp)
    #     ind = temp.argmin()
    #     inds.append(ind)
    # 这样不可行，应该先取 距离近的点之后比较光谱角
    # 在每个特征点附近，选取最接近的特征点
    # 计算特征点的距离
    #



