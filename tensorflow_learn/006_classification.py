import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

__author__ = 'wangj'
__date__ = '2017/10/04 00:04'


def add_layer(inputs, in_size, out_size, activation_func=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_func is None:
        out_puts = Wx_plus_b
    else:
        out_puts = activation_func(Wx_plus_b)
    return out_puts


def main():
    # 读数据，one_hot表示将矩阵处理为行向量，即28*28 => 1*784
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    xs = tf.placeholder(dtype=tf.float32, shape=[None, 784])  # 28*28
    ys = tf.placeholder(dtype=tf.float32, shape=[None, 10])

    # add output layer
    l1 = add_layer(xs, 784, 50, activation_func=tf.nn.sigmoid)
    prediction = add_layer(l1, 50, 10, activation_func=tf.nn.softmax)

    # the error between prediction and real_data
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    def compute_accuracy(v_xs, v_ys):
        y_pre = sess.run(prediction, feed_dict={xs: v_xs})
        correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
        return result

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for i in range(1001):
            batch_xs, batch_ys = mnist.train.next_batch(100)
            sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys})
            if i % 50 == 0:
                print(compute_accuracy(mnist.test.images, mnist.test.labels))


if __name__ == '__main__':
    main()
