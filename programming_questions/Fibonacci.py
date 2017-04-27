#!python3
# -*- coding:utf-8 -*-

def Fibonacci(n):
    if n == 0:
        return 0
    count, a, b = 1, 0, 1
    while True:
        a, b = b, a+b
        count += 1
        if count >= n:
            return b

    
    

if __name__ == '__main__':
    print(Fibonacci(0))
    print(Fibonacci(3))