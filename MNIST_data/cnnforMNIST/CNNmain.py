import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

__author__ = 'wangj'
__date__ = '2018/05/05 01:26'


CKPT_DIR = 'ckpt'


def main():
    pass


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    # stride [1, x_movement, y_movement, 1]
    # Must have strides[0] = strides[3] = 1
    return tf.nn.conv2d(x, W, [1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


if __name__ == '__main__':
    mnist = input_data.read_data_sets('../MNIST_data', one_hot=True)
    global_step = tf.Variable(0, trainable=False)

    # define placeholder for inputs to network
    x = tf.placeholder(tf.float32, [None, 784])  # 28x28
    y_ = tf.placeholder(tf.float32, [None, 10])
    keep_prob = tf.placeholder(tf.float32)  # dropout 参数
    x_image = tf.reshape(x, [-1, 28, 28, 1])
    # print(x_image.shape)  # [n_samples, 28,28,1]

    # conv1 layer ##
    W_conv1 = weight_variable([5, 5, 1, 32])  # patch 5x5, in size 1, out size 32
    b_conv1 = bias_variable([32])
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)  # output size 28x28x32  28/1
    h_pool1 = max_pool_2x2(h_conv1)  # output size 14x14x32  28/2

    # conv2 layer
    W_conv2 = weight_variable([5, 5, 32, 64])  # patch 5x5, in size 32, out size 64
    b_conv2 = bias_variable([64])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)  # output size 14x14x64
    h_pool2 = max_pool_2x2(h_conv2)  # output size 7x7x64

    # full connect layer 1
    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])
    # [n_samples, 7, 7, 64] ->> [n_samples, 7*7*64]
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    # full connect layer 2
    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])
    y_pre = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y_, logits=y_pre))
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy, global_step=global_step)

    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    sess = tf.Session()


    # tf.train.Saver是用来保存训练结果的。
    # max_to_keep 用来设置最多保存多少个模型，默认是5
    # 如果保存的模型超过这个值，最旧的模型将被删除

    # 总的训练次数
    all_steps = 10000
    # 记录训练次数, 初始化为0
    step = 0
    # 每隔1000步保存模型
    save_interval = 1000

    saver = tf.train.Saver(max_to_keep=10)
    sess.run(tf.global_variables_initializer())

    ckpt = tf.train.get_checkpoint_state(CKPT_DIR)
    if ckpt and ckpt.model_checkpoint_path:
        saver.restore(sess, ckpt.model_checkpoint_path)
        # 读取网络中的global_step的值，即当前已经训练的次数
        step = sess.run(global_step)
        print('Continue form-----')
        print('------------->Minibatch Step:', step)

    batch_size = 100

    while step < all_steps:
        # 从数据集中获取 输入和标签(也就是答案)
        x_train, y_train = mnist.train.next_batch(batch_size)
        # loss只是为了看到损失的大小，方便打印
        _, loss = sess.run([train_step, cross_entropy], feed_dict={
            x: x_train,
            y_: y_train,
            keep_prob: 0.5
        })
        step = sess.run(global_step)
        # 打印 loss，训练过程中将会看到，loss有变小的趋势
        # 代表随着训练的进行，网络识别图像的能力提高
        # 但是由于网络规模较小，后期没有明显下降，而是有明显波动
        if step % 1000 == 0:
            print('第{0:5d}步，当前loss：{1:.2f}'.format(step, loss))

        # 模型保存在ckpt文件夹下
        # 模型文件名最后会增加global_step的值，比如1000的模型文件名为 model-1000
        if step % save_interval == 0:
            saver.save(sess, CKPT_DIR + '/model', global_step=step)

    test_x = mnist.test.images
    test_label = mnist.test.labels
    accuracy = sess.run(accuracy, feed_dict={
        x: test_x,
        y_: test_label,
        keep_prob:1
    })
    print("准确率: {0:.2f}，共测试了{1:d}张图片 ".format(accuracy, len(test_label)))



