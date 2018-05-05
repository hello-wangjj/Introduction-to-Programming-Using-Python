import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

__author__ = 'wangj'
__date__ = '2018/05/04 17:01'


def main():
    pass


if __name__ == '__main__':
    mnist = input_data.read_data_sets('../MNIST_data', one_hot=True)

    x = tf.placeholder(tf.float32, shape=[None, 784])
    y_ = tf.placeholder(tf.float32, shape=[None, 10])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    y = tf.matmul(x, W) + b
    # cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=y, labels=y_))
    cross_entropy = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits_v2(logits=y, labels=y_))
    # softmax_cross_entropy_with_logits_v2 相当于先softmax之后 在reduce_sum
    train_step = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cross_entropy)
    for i in range(5000):
        x_train, y_train = mnist.train.next_batch(100)
        _, loss = sess.run([train_step, cross_entropy], feed_dict={
            x: x_train,
            y_: y_train
        })
        # 打印 loss，训练过程中将会看到，loss有变小的趋势
        # 代表随着训练的进行，网络识别图像的能力提高
        # 但是由于网络规模较小，后期没有明显下降，而是有明显波动
        if (i + 1) % 10 == 0:
            print('第{0:5d}步，当前loss：{1}'.format(i + 1, loss))

    predict = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    # tf.cast 类型转换 函数
    accuracy = tf.reduce_mean(tf.cast(predict, dtype=tf.float32))
    accuracy = sess.run(accuracy, feed_dict={
        x: mnist.test.images,
        y_: mnist.test.labels

    })
    print("准确率: {0:.2f}，共测试了{1:d}张图片 ".format(accuracy, len(mnist.test.labels)))
