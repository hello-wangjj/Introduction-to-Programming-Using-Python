"""
栈实现队列，队列实现栈
"""


class soloution:
    '''
        解决方法,2个栈实现队列
    '''

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


class soloution2(object):
    '''
        解决方法,2个队列实现栈
    '''
    def __init__(self):
        # super保证只初始化一次
        super(soloution2, self).__init__()
        self.deque1 = []
        self.deque2 = []

    def push(self, node):
        self.deque1.append(node)

    def pop(self):
        while len(self.deque1) > 1:
            self.deque2.append(self.deque1.pop(0))
        head = self.deque1.pop()
        while len(self.deque2) > 0:
            self.deque1.append(self.deque2.pop(0))
        return head


if __name__ == '__main__':
    s = soloution2()
    s.push(1)
    s.push(2)
    print(s.pop())
    s.push(3)
    print(s.pop())
