def main():
	n=eval(input('please input n nonnegative integer: '))
	print('Factorial of',n,'is',factorial(n))


def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

if __name__=='__main__':
	main()