import tensorflow as tf
import numpy as np

__author__ = 'wangj'
__date__ = '2017/12/19 15:07'


def main():
    # 数据集数量
    test_count = 10
    # 变量数
    param_count = 5
    t_x = np.floor(1000 * np.random.random([test_count, param_count]), dtype=np.float32)
    # 要求的值
    t_w = np.floor(1000 * np.random.random([param_count, 1]), dtype=np.float32)
    # t_bias = np.floor(np.zeros([1, 1]) + 0.1, dtype=np.float32)
    # 根据公式 t_y = t_x*t_w+3 计算t_y
    t_y = t_x.dot(t_w) + 0.5
    print(t_x)
    print(t_w)
    print(t_y)
    # x 是输入量，对应 t_x，用于训练输入，在训练过程中，由外部提供，因此是 placeholder 类型
    x = tf.placeholder(dtype=tf.float32, shape=[test_count, param_count])
    y = tf.placeholder(dtype=tf.float32, shape=[test_count, 1])
    # 以 TensorFlow 变量形式定义结果 w：
    w = tf.Variable(np.zeros(param_count, dtype=np.float32).reshape((param_count, 1)), tf.float32)
    bias = tf.Variable(np.zeros((1, 1))+0.1, dtype=tf.float32)
    curr_y = tf.matmul(x, w) + bias
    loss = tf.reduce_sum(tf.square(t_y - curr_y))
    optimizer = tf.train.GradientDescentOptimizer(0.00000001)
    train = optimizer.minimize(loss)
    LOSS_MIN_VALUE = tf.constant(1e-5)
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        run_count = 0
        last_loss = 0
        while True:
            run_count += 1
            sess.run(train, feed_dict={x: t_x, y: t_y})
            curr_loss, is_ok = sess.run([loss, loss < LOSS_MIN_VALUE], feed_dict={x: t_x, y: t_y})
            if run_count % 100 == 0:
                print("运行{0}次，last_loss={1}, loss={2}".format(run_count, last_loss, curr_loss))
            if last_loss == curr_loss:
                break
            last_loss = curr_loss
            if is_ok:
                break
        curr_W, curr_bias, curr_loss = sess.run([w, bias, loss], feed_dict={x: t_x, y: t_y})
        print("t_w:{}\n nw:{}\n fix_w:{} \nloss:{} \nfix_w_loss:{}".format(t_w, curr_W, np.round(curr_W),
                                                                   curr_loss,
                                                                   np.sum(np.square(t_w - np.round(curr_W)))))


if __name__ == '__main__':
    main()