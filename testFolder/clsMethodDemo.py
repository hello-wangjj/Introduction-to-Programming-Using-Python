class Counter(object):
    """
    一个计数器类
    """
    cnt = 0
    def __init__(self):
        pass

    @classmethod
    def show(cls):
        print('cnt:{}.'.format(cls.cnt))
    @classmethod
    def inc(cls):
        """计数值加一"""
        cls.cnt += 1
    @classmethod
    def dec(cls):
        """计数值减一"""
        cls.cnt -= 1
    

if __name__ == '__main__':
    Counter.inc()
    Counter.show()
    Counter.inc()
    Counter.show()
    Counter.dec()
    Counter.show()
    c1 = Counter()
    c1.show()
    c2 = Counter()
    c2.show()
    c1.inc()
    c1.show()
    c2.show()