def main():
	filename=input('enter a filename: ').strip()
	handle=open(filename,'r')

	counts=26*[0]
	for line in handle:
		countLetter(line.lower(),counts)
	for i in range(len(counts)):
		if counts[i]!=0:
			print((chr(ord('a')+i))+' appears '+(str(counts[i]))+(' time' if counts[i]==1 else ' times'))

	handle.close()

def countLetter(line,counts):
	for ch in line:
		if ch.isalpha():
			counts[ord(ch)-ord('a')]+=1
if __name__=='__main__':
	main()