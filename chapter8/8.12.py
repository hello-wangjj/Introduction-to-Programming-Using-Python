def main():
	genome=input('please input a string:')

	found=False
	start=-1
	for i in range(len(genome)-2):
		triplet=genome[i:i+3]
		if triplet=='ATG':
			start=i+3
		elif (triplet=='TAG' or triplet=='TAA' or triplet=='TGA') and start!=-1:
			gene=genome[start:i]
			if len(gene)%3==0:
				found=True
				print(gene)
				start=-1
	if not found:
		print('no gene is found')
main()


