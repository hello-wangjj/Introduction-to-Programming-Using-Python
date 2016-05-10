#回文检测

def main():
	s=input('Enter a string: ').strip()
	if isPalindrome(s):
		print(s,'is a palindrome')
	else:
		print(s,'is not a palindrome')

def isPalindrome(s):
	low=0
	high=len(s)-1

	while  low<high:
		# pass
		if s[low]!=s[high]:
			return False
		else:
			low+=1
			high-=1
	return True

if __name__=='__main__':
	main()
	L = ['Adam', 'Lisa', 'Bart', 'Paul']

	#zip 和 enumerate
	for index, name in zip(range(1,5),L):
    print index, '-', name
