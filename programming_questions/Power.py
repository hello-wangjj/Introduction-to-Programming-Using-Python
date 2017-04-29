#给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方
def Power(base, exponent):
    if base == 0:
        return 0
    elif base == 1:
        return 1
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return pow(base, exponent)


if __name__ == '__main__':
    print(Power(1.2,2))