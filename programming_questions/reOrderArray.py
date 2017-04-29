# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

def main(array):
    odd = []
    even = []
    for i in array:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    odd.extend(even)
    return odd
    

if __name__ == '__main__':
    print(main([1,3,2,4,11,5,6]))