import sys, os
__author__ = 'wangj'
__date__ = '2017/08/31 19:30'


def main():
    path = os.path.dirname(__file__)
    print('/'.join(path.split('/')[:-1]))
    open('tmp/documents_feature.txt', 'w')


if __name__ == '__main__':
    main()