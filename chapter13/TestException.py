def main():
	try:
		number1,number2=eval(input('please input two numbers,separated by a comma: '))
		result=number1/number2
		print('Result is',result)
	except ZeroDivisionError:
		print('Division by zero')
	except SyntaxError:
		print('a comma may be missing in the input')
	except :
		print('Somthing wrong in the input')
	else :
		print('no exceptions')
	finally:
		print('the finally clause is executed')

if __name__=='__main__':
	main()