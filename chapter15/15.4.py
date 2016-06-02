def main():
	# pass
	for i in range(1,10+1):
		print(m(i))

def m(i):
	# pass
	if i==1:
		return 1
	else:
		return m(i-1)+1/i


if __name__=='__main__':
	main()