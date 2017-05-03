#输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        node = []
        while pHead1 != None and pHead2 != None:
            if pHead1.val < pHead2.val:
                node.append(pHead1)
                pHead1 = pHead1.next
            else:
                node.append(pHead2)
                pHead2 = pHead2.next
        while pHead1 != None:
            node.append(pHead1);
            pHead1 = pHead1.next
        while pHead2 != None:
            node.append(pHead2)
            pHead2 = pHead2.next
        if node == []:
            return None
        for i in range(len(node)-1):
            node[i].next = node[i+1]
        return node[0]