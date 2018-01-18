import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pyswarms as pso

__author__ = 'wangj'
__date__ = '2018/01/14 21:31'


def main():
    pass


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


if __name__ == '__main__':
    img001, des_001 = save_sift_feature('images/65hz002.bmp')
    img002, des_002 = save_sift_feature('images/65hz002.bmp')
    cv.imwrite('001.jpg', img001)
    cv.imwrite('002.jpg', img002)
    key_point_001 = des_001[0]
    key_point_feature_001 = des_001[1]
    key_point_002 = des_002[0]
    key_point_feature_002 = des_002[1]

    # Set-up hyperparameters
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

    # Call instance of PSO
    optimizer = pso.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)

    # func 特征 矩阵的 距离





