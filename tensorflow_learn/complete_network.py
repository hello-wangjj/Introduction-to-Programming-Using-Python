import tensorflow as tf
from numpy.random import RandomState

batch_size = 8
w1 = tf.Variable(tf.random_normal([2,3],seed=1,stddev=1.0))
w2 = tf.Variable(tf.random_normal([3,1],seed=1,stddev=1.0))

x = tf.placeholder(tf.float32, shape=(None,2), name='x-input')
y_hat = tf.placeholder(tf.float32, shape=(None,1), name='y-input')

# 定义前向传播过程
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 定义损失函数 和 反向传播算法
cross_entropy = -tf.reduce_mean(y_hat * tf.log(tf.clip_by_value(y,1e-10,1.0)))
train_step = tf.train.AdagradOptimizer(0.010).minimize(cross_entropy)

# 随机生成模拟数据
rdm = RandomState(1)
data_size = 128
X = rdm.rand(data_size,2)

# 定义规则来给出样本标签
Y = [[int(x1+x2<1)] for x1,x2 in X]

init = tf.global_variables_initializer()
# 创建会话
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(w1))
    print(sess.run(w2))

    # 设置训练的轮数
    Steps = 5000
    for i in range(Steps):
        start = (i*batch_size)%data_size
        end = min(start+batch_size,data_size)
        sess.run(train_step, feed_dict={x:X[start:end],y_hat:Y[start:end]})

        if i%1000 ==0:
            total_cross_entropy = sess.run(cross_entropy, feed_dict={x:X,y_hat:Y})
            print('after {} training steps,cross_entropy is {}'.format(i,total_cross_entropy))

