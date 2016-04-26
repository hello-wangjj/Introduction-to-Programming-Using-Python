n=eval(input('please enter a number between 0 and 1000:'))
#个位
a=n%10
#前2wei
n=n//10
#十位
b=n%10
#百位
c=n//10
m=a+b+c
print ('the sum is:',m)