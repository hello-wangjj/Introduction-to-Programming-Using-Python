import tensorflow as tf
from numpy.random import RandomState

__author__ = 'wangj'
__date__ = '2017/10/06 16:31'


def main():
    batch_size = 8
    x = tf.placeholder(dtype=tf.float32, shape=[None, 2], name='x-input')
    y = tf.placeholder(dtype=tf.float32, shape=[None, 1], name='y-input')

    w1 = tf.Variable(tf.random_normal([2, 1], stddev=1, seed=1))
    y_hat = tf.matmul(x, w1)

    # loss
    loss_less = 10
    loss_more = 1
    loss = tf.reduce_sum(tf.where(tf.greater(y, y_hat), (y - y_hat) * loss_more, (y_hat - y) * loss_less))

    train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

    rdm = RandomState(1)

    dataset_size = 128
    X = rdm.rand(dataset_size, 2)
    Y = [[x1 + x2 + rdm.rand() / 10 - 0.05] for (x1, x2) in X]

    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run(init_op)
        Steps = 5001
        for i in range(Steps):
            start = (i * batch_size) % dataset_size
            end = min(start + batch_size, dataset_size)
            sess.run(train_step, feed_dict={x: X[start:end], y: Y[start:end]})
            if i % 100 == 0:
                print(sess.run(w1))


if __name__ == '__main__':
    main()
