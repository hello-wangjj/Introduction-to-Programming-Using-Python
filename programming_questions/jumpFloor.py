#! python3
# -*- coding:utf-8 -*-
#一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# way1
def jumpFloor(number):
    if number == 1:
        return 1
    if number == 2:
        return 2
    else:
        return jumpFloor(number-1)+jumpFloor(number-2)
#way2
def jumpFloor_2(n):
    count, a, b = 0, 1, 1
    while True:
        a, b = b, a+b
        count += 1
        if count >= n:
            return a
#way3
def jumpFloor_3(number):
        # write code here
        if number <= 0:
            return 1
        elif number <= 2:
            return number
        else:
            a,b = 1,2
            for i in range(2,number):
                tmp = a+b
                a=b
                b=tmp
                #a,b = b,tmp
            return b



if __name__ == '__main__':
    print(jumpFloor(1))
    print(jumpFloor(2))
    print(jumpFloor(3))
    print(jumpFloor(4))
    print(jumpFloor(5))
    print('way2')
    print(jumpFloor_2(1))
    print(jumpFloor_2(2))
    print(jumpFloor_2(3))
    print(jumpFloor_2(4))
    print(jumpFloor_2(5))
    print('way3')
    print(jumpFloor_3(1))
    print(jumpFloor_3(2))
    print(jumpFloor_3(3))
    print(jumpFloor_3(4))
    print(jumpFloor_3(5))