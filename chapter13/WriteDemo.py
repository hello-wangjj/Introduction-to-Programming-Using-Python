def main():
	outfile=open('Presidents.txt','a')

	outfile.write('Bill Clinton\n')
	outfile.write('George Bush\n')
	outfile.write('Barack Obama\n')

	outfile.close()

if __name__=='__main__':
	main()