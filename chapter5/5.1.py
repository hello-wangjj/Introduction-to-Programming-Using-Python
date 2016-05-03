positive=0
positiveSum=0
negative=0
negativeSum=0
total=0
isNum=True
while isNum:
	# pass
	number=eval(input('please input a number, if 0 will stop: '))
	if number==0:
		break
	elif number>0:
		positive+=1
		# positiveSum+=number
		total+=number
	elif number<0:
		negative+=1
		# negativeSum+=number
		total+=number
print ('the number of positives is',positive)
print ('the number of negatives is',negative)
print ('the total is',total)
print ('the average is',total/(positive+negative))
