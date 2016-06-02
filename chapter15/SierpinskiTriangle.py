import tkinter as tk

class SierpinskiTriangle(object):
	"""docstring for SierpinskiTriangle"""
	def __init__(self):
		super(SierpinskiTriangle, self).__init__()
		# self.arg = arg
		window=tk.Tk()
		window.title('Sierpinski Triangle')

		self.width=200
		self.height=200
		self.canvas=tk.Canvas(window,width=self.width,height=self.height)
		self.canvas.pack()

		frame1=tk.Frame(window)
		frame1.pack()

		tk.Label(frame1,text='enter a order').pack(side=tk.LEFT)
		self.order=tk.StringVar()
		tk.Entry(frame1,textvariable=self.order,justify=tk.RIGHT).pack(side=tk.LEFT)
		tk.Button(frame1,text='Display Sierpinski Triangle',command=self.display).pack(side=tk.LEFT)
		window.mainloop()

	def display(self):
		self.canvas.delete('line')
		p1=[self.width/2,10]
		p2=[10,self.height-10]
		p3=[self.width-10,self.height-10]
		self.displayTriangles(int(self.order.get()),p1,p2,p3)
		

	def displayTriangles(self,order,p1,p2,p3):
		if order==0:
			#draw a trangle to connect three points
			self.drawLine(p1,p2)
			self.drawLine(p2,p3)
			self.drawLine(p3,p1)
		else:
			#get the mid point  of each triangle's edge
			p12=self.midPoint(p1,p2)
			p23=self.midPoint(p2,p3)
			p31=self.midPoint(p3,p1)

			self.displayTriangles(order-1, p1, p12, p31)
			self.displayTriangles(order-1, p12, p2, p23)
			self.displayTriangles(order-1, p31, p23, p3)

	def drawLine(self,p1,p2):
		self.canvas.create_line(p1[0],p1[1],p2[0],p2[1],tags='line')

	def midPoint(self,p1,p2):
		p=2*[0]
		p[0]=(p1[0]+p2[0])/2
		p[1]=(p1[1]+p2[1])/2
		return p
if __name__=='__main__':
	SierpinskiTriangle()




