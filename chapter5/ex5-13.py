#prime number

number_of_primes=50
number_of_primes_per_line=10
count=0
number=2
print ('the first 50 prime numbers are')

while  count<number_of_primes:
	# pass
	isPrime=True

	divisor=2
	while divisor<=number/2:
		# pass
		if number%divisor==0:
			isPrime=False
			break
		divisor+=1
	if isPrime:
		count+=1
		print(format(number,'5d'),end='')
		if count%number_of_primes_per_line==0:
			print()
	number+=1
