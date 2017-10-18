__author__ = 'wangj'
__date__ = '2017/10/18 21:52'
"""
现在有一棵合法的二叉树，树的节点都是用数字表示，
现在给定这棵树上所有的父子关系，求这棵树的高度
"""


def main():
    n = int(input())
    tree = {'0': [1, 0]}
    for i in range(n - 1):
        root, child = input().strip().split(' ')
        if root in tree.keys() and tree[root][1] < 2:
            tree[root][1] += 1
            tree[child] = [tree[root][0] + 1, 0]
    print(max(i[0] for i in tree.values()))


if __name__ == '__main__':
    main()
