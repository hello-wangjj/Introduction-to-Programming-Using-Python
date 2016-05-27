import math
class Circle(object):
	"""docstring for Circle"""
	def __init__(self, radius):
		super(Circle, self).__init__()
		# self.arg = arg
		self.setRadius(radius)

	def setRadius(self,radius):
		if radius<0:
			raise RuntimeError('negative radius')
		else:
			self.__radius=radius
	def getArea(self):
		return self.__radius*self.__radius*math.pi

if __name__=='__main__':
	try:
		c1=Circle(5)
		print('C1 area is ',c1.getArea())
		c2=Circle(-1)
		print('C2 area is ',c2.getArea())
		c3=Circle(0)
		print('C3 area is ',c3.getArea())
	except RuntimeError:
		print('invalid radius')

		