#!python3
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '2017042521:52'


def printListFromTailToHead(listNode):
    l = []
    head = listNode
    while head:
        l.insert(0, head.val)
        head = head.next
    return l

print(printListFromTailToHead([1, 2, 3]))
