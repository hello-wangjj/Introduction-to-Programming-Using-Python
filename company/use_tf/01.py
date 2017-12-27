import tensorflow as tf
import numpy as np

__author__ = 'wangj'
__date__ = '2017/12/19 01:14'


def main():
    t_x = np.floor(10 * np.random.random([5]), dtype=np.float32)
    print(t_x)
    t_y = t_x * 3.0 + 8
    print(t_y)
    x = tf.placeholder(tf.float32)
    y = tf.placeholder(tf.float32)
    a = tf.Variable(0.0)
    b = tf.Variable(0.0)
    curr_y = x * a + b
    loss = tf.reduce_sum(tf.square(curr_y - y))
    optimizer = tf.train.GradientDescentOptimizer(0.001)
    train = optimizer.minimize(loss)
    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)
    sess.run(train, feed_dict={x: t_x, y: t_y})
    for i in range(10000):
        sess.run(train, feed_dict={x: t_x, y: t_y})
        if i % 100 == 0:
            print(sess.run([a, b, loss], feed_dict={x: t_x, y: t_y}))


if __name__ == '__main__':
    main()
