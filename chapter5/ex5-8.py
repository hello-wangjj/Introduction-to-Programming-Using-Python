n1=eval(input('enter first intergers:'))
n2=eval(input('enter second intergers:'))

#公约数
gcd=1
k=2
while k<=n1 and k<=n2:
	# pass
	if n1%k==0 and n2%k==0:
		gcd=k
	k+=1
print ('the greast common divisor for' ,n1,'and',n2,'is',gcd)