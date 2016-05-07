class TV(object):
	"""docstring for TV"""
	def __init__(self):
		super(TV, self).__init__()
		# self.arg = arg
		#default setting
		self.channel=1
		self.volumnLevel=1
		self.on=False

	def turnOn(self):
		self.on=True
	def turnOff(self):
		self.on=False
	def getChannel(self):
		# pass
		return self.channel
	def setChannel(self,channel):
		if self.on and 1<=self.channel<=120:
			self.channel=channel

	def getVolumnLevel(self):
		return self.volumnLevel

	def setVolumnLevel(self,volumnLevel):
		if self.on and 1<=self.volumnLevel<=7:
			self.volumnLevel=volumnLevel

	def channelUp(self):
		if self.on and self.channel<120:
			self.channel+=1
	def channelDown(self):
		if self.on and self.channel>1:
			self.channel-=1

	def volumnUp(self):
		if self.on and self.volumnLevel<7:
			self.volumnLevel+=1

	def volumnDown(self):
		if self.on and self.volumnLevel>1:
			self.volumnLevel-=1
def main():
	tv1=TV()
	tv1.turnOn()
	tv1.setChannel(30)
	tv1.setVolumnLevel(3)

	tv2=TV()
	tv2.turnOn()
	tv2.channelUp()
	tv2.channelUp()
	tv2.volumnUp()

	print("tv1's channel is ",tv1.getChannel(),"and tv1's volumn level is ",tv1.getVolumnLevel())
	print("tv2's channel is ",tv2.getChannel(),"and tv2's volumn level is ",tv2.getVolumnLevel())


if __name__=='__main__':
	main()