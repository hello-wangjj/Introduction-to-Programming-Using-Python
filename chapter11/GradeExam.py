def main():
	answers=[
		['a','b','a','c','c','d','e','e','a','d'],
		['d','b','a','b','c','a','e','e','a','d'],
		['e','d','d','a','c','b','e','e','a','d'],
		['c','b','a','e','d','c','e','e','a','d'],
		['a','b','d','c','c','d','e','e','a','d'],
		['b','b','e','c','c','d','e','e','a','d'],
		['b','b','a','c','c','d','e','e','a','d'],
		['e','b','e','c','c','d','e','e','a','d']
	]

	keys=['d','b','d','c','c','d','a','e','a','d']

	correctCounts=0
	for i in range(len(answers)):
		 correctCounts=0
		 for j in range(len(answers[i])):
		 	if keys[j]==answers[i][j]:
		 		correctCounts+=1
		 print('Student ',i,"'s correct count is ",correctCounts)

main()