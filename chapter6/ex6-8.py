def decimalToHex(decimalValue):
	hex=''
	while  decimalValue!=0:
		# pass
		hexValue=decimalValue%16
		hex=toHexChar(hexValue)+hex
		decimalValue=decimalValue//16
	return hex

def toHexChar(hexValue):
	if hexValue<10:
		return str(hexValue)
	else:
		l={11:'B',10:'A',12:'C',13:'D',14:'E',15:'F'}
		# return str(l[hexValue])
		return l[hexValue]

if __name__=='__main__':
	decimalValue=eval(input('please input a number: '))
	print ('the hex number of decimal',decimalValue,'is',decimalToHex(decimalValue))
