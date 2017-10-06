import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

__author__ = 'wangj'
__date__ = '2017/10/05 11:33'


def add_layer(inputs, in_size, out_size, layer_name, activation_func=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size], dtype=tf.float64), dtype=tf.float64)
    biases = tf.Variable(tf.zeros([1, out_size], dtype=tf.float64) + 0.1, dtype=tf.float64)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_func is None:
        out_puts = Wx_plus_b
    else:
        out_puts = activation_func(Wx_plus_b)
    tf.summary.histogram(layer_name + '/out_puts', out_puts)
    return out_puts


def main():
    digits = load_digits()
    X = digits.data
    y = digits.target
    y = LabelBinarizer().fit_transform(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    xs = tf.placeholder(dtype=tf.float64, shape=[None, 64])
    ys = tf.placeholder(dtype=tf.float64, shape=[None, 10])

    # add layer
    l1 = add_layer(X_train, 64, 100, 'l1', activation_func=tf.nn.tanh)
    prediction = add_layer(l1, 100, 10, 'l2', activation_func=tf.nn.softmax)

    # loss
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_train * tf.log(prediction), reduction_indices=[1]))
    tf.summary.scalar('loss', cross_entropy)
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        merged = tf.summary.merge_all()
        # summary writer goes in here
        train_writer = tf.summary.FileWriter('./logs/train', sess.graph)
        test_writer = tf.summary.FileWriter('./logs/test', sess.graph)
        sess.run(init)
        for i in range(501):
            sess.run(train_step, feed_dict={xs: X_train, ys: y_train})
            if i % 50 == 0:
                train_result = sess.run(merged, feed_dict={xs: X_train, ys: y_train})
                test_result = sess.run(merged, feed_dict={xs: X_test, ys: y_test})
                train_writer.add_summary(train_result, i)
                test_writer.add_summary(test_result, i)


if __name__ == '__main__':
    main()
