import pickle
def main():
	outfile=open('pickle.dat','wb')
	pickle.dump(45, outfile)
	pickle.dump(56.6, outfile)
	pickle.dump('programming is fun', outfile)
	pickle.dump([1,2,3,4], outfile)
	outfile.close()

	infile=open('pickle.dat','rb')
	print(pickle.load(infile))
	print(pickle.load(infile))
	print(pickle.load(infile))
	print(pickle.load(infile))
	infile.close()
if __name__=='__main__':
	main()