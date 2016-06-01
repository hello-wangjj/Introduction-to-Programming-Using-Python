def main():
	index=eval(input('enter a index for a fibonacci number : '))
	print('the fibonacci number at index',index,'is',fib(index))

def fib(index):
	if index==0:
		return 0
	elif index==1:
		return 1
	else :
		return fib(index-1)+fib(index-2)

if __name__=='__main__':
	main()