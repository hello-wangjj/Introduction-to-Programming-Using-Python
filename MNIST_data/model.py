import numpy as np
import tensorflow as tf

__author__ = 'wangj'
__date__ = '2018/05/02 19:55'


def main():
    pass


def softmax(x):
    """
    Compute the softmax function for each row of the input x.
    :param x: A N dimensional vector or M x N dimensional numpy matrix.
    :return:
    """
    origin_shape = x.shape
    if len(origin_shape) > 1:
        # matrix
        # lambda 函数
        # 分子
        exp_matrix = lambda x: np.exp(x - np.max(x))
        # 分母
        deno = lambda x: 1.0 / np.sum(x)
        x = np.apply_along_axis(exp_matrix, 1, x)
        denominator = np.apply_along_axis(deno, 1, x)

        if len(denominator.shape) == 1:
            denominator = denominator.reshape((denominator.shape[0], 1))
        x = x * denominator

    else:
        # vector
        x_max = np.max(x)
        x = x - x_max
        numerator = np.exp(x)
        denominator = 1.0 / np.sum(numerator)
        x = x * denominator

    assert x.shape == origin_shape
    return x


class Network(object):
    def __init__(self, learning_rate=0.001, ):
        # 学习速率
        self.learning_rate = learning_rate
        # 输入张量 28 * 28 = 784个像素的图片一维向量
        self.x = tf.placeholder(tf.float32, [None, 784])
        # 标签值，即图像对应的结果，如果对应数字是8，则对应label是 [0,0,0,0,0,0,0,0,1,0]
        # 这种方式称为 one-hot编码
        # 标签是一个长度为10的一维向量，值最大的下标即图片上写的数字
        self.label = tf.placeholder(tf.float32, [None, 10])

        # 权重，初始化 正态分布
        self.w = tf.Variable(tf.random_normal([784, 10]))
        # 偏置 bias， 初始化 正态分布
        self.b = tf.Variable(tf.random_normal([10]))
        # 输出 y = softmax(X * w + b)
        self.y = tf.nn.softmax(tf.matmul(self.x, self.w) + self.b)
        # 损失，即交叉熵，最常用的计算标签(label)与输出(y)之间差别的方法
        self.loss = - tf.reduce_sum(self.label * tf.log(self.y + 1e-10))
        # 反向传播，采用梯度下降的方法。调整w与b，使得损失(loss)最小
        # loss越小，那么计算出来的y值与 标签(label)值越接近，准确率越高
        self.train = tf.train.GradientDescentOptimizer(self.learning_rate).minimize(self.loss)

        # 以下代码验证正确率时使用
        # argmax 返回最大值的下标，最大值的下标即答案
        # 例如 [0,0,0,0.9,0,0.1,0,0,0,0] 代表数字3
        predict = tf.equal(tf.argmax(self.label, 1), tf.argmax(self.y, 1))

        # predict -> [true, true, true, false, false, true]
        # reduce_mean即求predict的平均数 即 正确个数 / 总数，即正确率
        self.accuracy = tf.reduce_mean(tf.cast(predict, dtype=tf.float32))


if __name__ == '__main__':
    x = np.array([[1, 2, 3], [4, 5, 6]])
    print(softmax(x))
