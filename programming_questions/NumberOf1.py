#输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
def NumberOf1(n):
    # write code here
    return sum([(n>>i & 1) for i in range(0,32)])

if __name__ == '__main__':
    print(NumberOf1(5))
    print(NumberOf1(-5))