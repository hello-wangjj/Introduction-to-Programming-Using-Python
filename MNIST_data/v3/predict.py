import numpy as np
from PIL import Image
import tensorflow as tf
from v2.model import Network

__author__ = 'wangj'
__date__ = '2018/05/03 22:04'
__doc__ = '''
使用tensorflow的模型来预测手写数字
输入是28 * 28像素的图片，输出是个具体的数字
'''


def main():
    pass


CKPT_DIR = 'ckpt'


class Predict(object):
    def __init__(self):
        self.net = Network(learning_rate=0.001)
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())

        # 加载模型
        self.restore()

    def restore(self):
        saver = tf.train.Saver()
        ckpt = tf.train.get_checkpoint_state(CKPT_DIR)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(self.sess, ckpt.model_checkpoint_path)
        else:
            raise FileNotFoundError('未保存模型')

    def predict(self, image_path):
        # 读图片并转为灰度
        img = Image.open(image_path).convert('L')
        flatten_img = np.reshape(img, 784)
        x = np.array([1 - flatten_img])
        y = self.sess.run(self.net.y, feed_dict={
            self.net.x:x
        })
        # 因为x只传入了一张图片，取y[0]即可
        # np.argmax()取得独热编码最大值的下标，即代表的数字
        print(image_path)
        print('        -> Predict digit', np.argmax(y[0]))


if __name__ == '__main__':
    app = Predict()
    app.predict('../test_images/3_001.png')
