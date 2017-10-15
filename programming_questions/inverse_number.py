"""
整数逆序
"""

from functools import reduce

number_s = input("please input a number:")
first_number = number_s[0]
if first_number == '-':
    number = int(number_s[1:])
else:
    number = int(number_s)
numlist = []

result = 0

while 1:
    if number == 0:
        break
    numlist.append(number % 10)
    number = int(number / 10)


def f(x, y):
    return x * 10 + y


number_res = str(reduce(f, numlist))
# number_res = ''.join(numlist)

if first_number == '-':
    number_res = int(first_number + number_res)
    if number_res < -2147483648:
        print(0)
    else:
        print(number_res)
else:
    if int(number_res) > 2147483647:
        print(0)
    else:
        print(number_res)
