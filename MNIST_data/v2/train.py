import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from v2.model import Network

__author__ = 'wangj'
__date__ = '2018/05/03 16:53'
__doc__ = '''
增加了模型的保存和继续训练
'''
# 定义模型存储的位置
CKPT_DIR = 'ckpt'


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
        self.data = input_data.read_data_sets(
            'E:\document\GitHub\Introduction-to-Programming-Using-Python\MNIST_data\MNIST_data', one_hot=True)

    def train(self):
        # batch_size 是指每次迭代训练，传入训练的图片张数。
        # 数据集小，可以使用全数据集，数据大的情况下，
        # 为了提高训练速度，用随机抽取的n张图片来训练，效果与全数据集相近
        # https://www.zhihu.com/question/32673260
        batch_size = 64

        # 总的训练次数
        train_step = 10000
        # 记录训练次数, 初始化为0
        step = 0
        # 每隔1000步保存模型
        save_interval = 1000

        # tf.train.Saver是用来保存训练结果的。
        # max_to_keep 用来设置最多保存多少个模型，默认是5
        # 如果保存的模型超过这个值，最旧的模型将被删除
        saver = tf.train.Saver(max_to_keep=10)

        ckpt = tf.train.get_checkpoint_state(CKPT_DIR)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(self.sess, ckpt.model_checkpoint_path)
            # 读取网络中的global_step的值，即当前已经训练的次数
            step = self.sess.run(self.net.global_step)
            print('Continue form-----')
            print('------------->Minibatch Step:', step)

        while step < train_step:
            # 从数据集中获取 输入和标签(也就是答案)
            x, label = self.data.train.next_batch(batch_size)
            # loss只是为了看到损失的大小，方便打印
            _, loss = self.sess.run([self.net.train, self.net.loss], feed_dict={
                self.net.x: x,
                self.net.label: label
            })
            step = self.sess.run(self.net.global_step)
            # 打印 loss，训练过程中将会看到，loss有变小的趋势
            # 代表随着训练的进行，网络识别图像的能力提高
            # 但是由于网络规模较小，后期没有明显下降，而是有明显波动
            if step % 1000 == 0:
                print('第{0:5d}步，当前loss：{1:.2f}'.format(step, loss))

            # 模型保存在ckpt文件夹下
            # 模型文件名最后会增加global_step的值，比如1000的模型文件名为 model-1000
            if step % save_interval == 0:
                saver.save(self.sess, CKPT_DIR + '/model', global_step=step)

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
