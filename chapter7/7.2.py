class Stock(object):
	"""docstring for Stock"""
	def __init__(self, symbol,name,previousClosingPrice,currentPrice):
		super(Stock, self).__init__()
		# self.arg = arg
		self.__symbol=symbol
		self.__name=name
		self.__previousClosingPrice=previousClosingPrice
		self.__currentPrice=currentPrice

	def getName(self):
		return self.__name
	def getSymbol(self):
		return self.__symbol
	def getPreviousClosingPrice(self,previousClosingPrice):
		return self.__previousClosingPrice
	def setPreviousClosingPrice(self,previousClosingPrice):
		self.__previousClosingPrice=previousClosingPrice
	def getCurrentPrice(self):
		return self.__currentPrice
	def setCurrentPrice(self,currentPrice):
		self.__currentPrice=currentPrice
	def getChangePercent(self):
		return (format((self.__currentPrice-self.__previousClosingPrice)*100\
			/self.__previousClosingPrice,'05.2f')+'%')
def main():
	stock=Stock('INTC', 'Intel Corporation', 20.5, 20.35)
	print ('the price change is',stock.getChangePercent())

if __name__=='__main__':
	main()


		