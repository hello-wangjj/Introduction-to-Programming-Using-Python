import random
number_of_trials=1000000
numberOfHits=0
for i in range(number_of_trials):
	x=random.random()*2-1
	y=random.random()*2-1
	if x**2+y**2<=1:
		numberOfHits+=1
pi=4*numberOfHits/number_of_trials
print ('PI is ',pi)