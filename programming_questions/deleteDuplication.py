# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
# 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        # 1.加一个头结点
        # 2.两个临时指针p,q
        # 3.找前后不相等的节点
        first = ListNode(-1)
        first.next = pHead
        p = pHead
        last = first
        while p and p.next:
            if p.val == p.next.val:
                val = p.val
                while p and p.val == val:
                    p = p.next
                last.next = p
            else:
                last = p
                p = p.next
        return first.next

    # way2
    def deleteDuplication2(self, pHead):
        # 先为链表创建一个头结点
        first = ListNode(-1)
        first.next =  pHead
        # 2.两个临时指针p,q
        p = first
        q = pHead
        while q:
            while q.next and q.next.val == q.val:
                q=q.next
            if p.next !=q:
                q = q.next
                p.next = q
            else:
                p = q
                q = q.next

        return first.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    s= Solution()
    print(s.deleteDuplication2(a).val)




