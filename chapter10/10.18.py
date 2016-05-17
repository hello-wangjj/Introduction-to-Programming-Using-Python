def main():
	queens=8*[-1]
	queens[0]=0

	k=1
	while  k>=0 and k <=7:
		# Find a position to place a queen in the kth row
		j = findPosition(k,queens)
		if j < 0:
			queens[k] = -1
			k -= 1 # back track to the previous row
		else:
			queens[k] = j
			k += 1

	printResult(queens)




def findPosition(k,queens):
	start=0 if queens[k]==-1 else (queens[k]+1)

	for j in range(start,8):
		if isValid(k,j,queens):
			return j
	return -1

def isValid(k,j,queens):
	for i in range(k):
		if queens[i]==j:
			return False

	row=k-1
	column=j-1
	while  row>=0 and column>=0:
		# pass
		if queens[row]==column:
			return False
		row-=1
		column-=1

	return True

def printResult(queens):
	for i in range(8):
		print(str(i) + ", " + str(queens[i]))
	print()

    # Display the output
	for i in range(8):
		for j in range(queens[i]):
			print("| ", end = "")
		print("|Q|", end = "")

		for j in range(queens[i] + 1, 8):
			print(" |", end = "")
		print()
      
main()