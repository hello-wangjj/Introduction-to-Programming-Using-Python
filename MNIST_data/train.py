import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from model import Network

__author__ = 'wangj'
__date__ = '2018/05/03 16:53'


class Train(object):
    def __init__(self):
        self.net = Network(learning_rate=0.001)

        # 初始化 session
        # Network() 只是构造了一张计算图，计算需要放到会话(session)中
        self.sess = tf.Session()

        # 初始化变量
        self.sess.run(tf.global_variables_initializer())
        # 读取训练和测试数据，这是tensorflow库自带的，不存在训练集会自动下载
        # 项目目录下已经下载好，删掉后，重新运行代码会自动下载
        # MNIST_data/train-images-idx3-ubyte.gz
        # MNIST_data/train-labels-idx1-ubyte.gz
        # MNIST_data/t10k-images-idx3-ubyte.gz
        # MNIST_data/t10k-labels-idx1-ubyte.gz
        self.data = input_data.read_data_sets('MNIST_data', one_hot=True)

    def train(self):
        # batch_size 是指每次迭代训练，传入训练的图片张数。
        # 数据集小，可以使用全数据集，数据大的情况下，
        # 为了提高训练速度，用随机抽取的n张图片来训练，效果与全数据集相近
        # https://www.zhihu.com/question/32673260
        batch_size = 64

        # 总的训练次数
        train_step = 5000

        # 开始训练
        for i in range(train_step):
            # 从数据集中获取 输入和标签(也就是答案)
            x, label = self.data.train.next_batch(batch_size)
            # 每次计算train，更新整个网络
            # loss只是为了看到损失的大小，方便打印
            _, loss = self.sess.run([self.net.train, self.net.loss], feed_dict={
                self.net.x: x,
                self.net.label: label
            })
            # 打印 loss，训练过程中将会看到，loss有变小的趋势
            # 代表随着训练的进行，网络识别图像的能力提高
            # 但是由于网络规模较小，后期没有明显下降，而是有明显波动
            if (i + 1) % 10 == 0:
                print('第{0:5d}步，当前loss：{1:.2f}'.format(i + 1, loss))

    def cal_accuracy(self):
        test_x = self.data.test.images
        test_label = self.data.test.labels
        # 注意：与训练不同的是，并没有计算 self.net.train
        # 只计算了accuracy这个张量，所以不会更新网络
        # 最终准确率约为0.83
        accuracy = self.sess.run(self.net.accuracy, feed_dict={
            self.net.x: test_x,
            self.net.label: test_label
        })
        print("准确率: {0:.2f}，共测试了{1:d}张图片 ".format(accuracy, len(test_label)))


def main():
    pass


if __name__ == '__main__':
    app = Train()
    app.train()
    app.cal_accuracy()
