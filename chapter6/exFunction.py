from random import randint

def getRandomCharacter(ch1,ch2):
	return chr(randint(ord(ch1),ord(ch2)))

def getRandomLowerCaseLetter():
	return getRandomCharacter('a', 'z')

def getRandomUpperCaseLetter():
	return getRandomCharacter('A', 'Z')

def getRandomDigitCharacter():
	return getRandomCharacter('0', '9')

def getRandomASCIICharacter():
	return chr(randint(0,127))
