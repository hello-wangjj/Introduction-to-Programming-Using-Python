__author__ = 'wangj'
__date__ = '2017/10/18 22:12'
"""
给定一个句子（只包含字母和空格）， 将句子中的单词位置反转，单词用空格分割, 
单词之间只有一个空格，前后没有空格。 
比如： （1） “hello xiao mi”-> “mi xiao hello”
"""


def main():
    s = input().strip().split(' ')[::-1]
    print(' '.join(s))


if __name__ == '__main__':
    main()
