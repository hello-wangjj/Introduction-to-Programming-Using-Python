# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
# 返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
-*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        pNode = pHead
        if pHead == None:
            return None
        self.connectnodes(pHead)
        self.connectrandomnodes(pHead)
        return self.reconnectnodes(pHead)
 
    # 复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面
    def connectnodes(self,pHead):
        pNode = pHead
        while (pNode):
            pClone = RandomListNode(0)
            pClone.label = pNode.label
            pClone.next = pNode.next
            pClone.random = None
 
            pNode.next = pClone
            pNode = pClone.next
 
    # 将复制后的链表中的复制结点的random指针链接到被复制结点random指针的后一个结点
    def connectrandomnodes(self,pHead):
        pNode = pHead
        while (pNode):
            pClone = pNode.next
            if pNode.random:
                pClone.random = pNode.random.next
 
            pNode = pClone.next
 
    # 拆分链表, 将原始链表的结点组成新的链表, 复制结点组成复制后的链表
    def reconnectnodes(self,pHead):
        pNode = pHead
        pHeadclone = pClone = pNode.next
        pNode.next = pClone.next
        pNode = pClone.next
 
        while pNode:
            pClone.next = pNode.next
            pClone = pClone.next
            pNode.next = pClone.next
            pNode = pNode.next
 
        return pHeadclone

# way2
class Solution2:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:return None
        cur = pHead
        #insert new node between origin listnode
        while cur:
            tmp = RandomListNode(cur.label)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        cur  = pHead
        # find the random
        while cur:
            tmp = cur.next
            if cur.random:tmp.random = cur.random.next
            cur = tmp.next
        # to two listNode
        cur = pHead
        res = pHead.next
        while cur.next:
            tmp = cur.next
            cur.next = tmp.next
            cur = tmp
        return res
# way3
class Solution3:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # write code here
        self.CloneNodes(pHead)
        self.Random(pHead)
        return self.Connect(pHead)
    # 参考的是剑指offer书本的代码，先复制链表与原链表在一起，然后把复制任意指针，最后分成奇数和偶数的链表
    def CloneNodes(self,pHead):
        pNode=pHead
        while pNode:
            pCloned=RandomListNode(pNode.label)
            pCloned.next=pNode.next
            pNode.next=pCloned
            pNode=pCloned.next
                           
    def Random(self,pHead):
        pNode=pHead
        while pNode:
            pCloned=pNode.next
            if pNode.random:
                pCloned.random=pNode.random.next
            pNode=pCloned.next
             
    def Connect(self,pHead):
        pNode=pHead
        pClonedHead=None
        pCloned=None
        if pHead:
            pClonedHead=pCloned=pNode.next
            pNode.next=pCloned.next
            pNode=pCloned.next
        while pNode:
            pCloned.next=pNode.next
            pCloned=pCloned.next
            pNode.next=pCloned.next
            pNode=pNode.next
        return pClonedHead