import FindNearestPoints

import tkinter as tk

radius=2
class NearsestGui(object):
	"""docstring for NearsestGui"""
	def __init__(self):
		super(NearsestGui, self).__init__()
		# self.arg = arg
		self.points=[]
		window=tk.Tk()
		window.title('Find Nearsest GUI')


		self.canvas=tk.Canvas(window,width=400,height=200)
		self.canvas.pack()

		self.canvas.bind('<Button-1>',self.addPoint)
		window.mainloop()


	def addPoint(self,event):
		# pass
		if not self.isToolCloseToOtherPoints(event.x,event.y):
			self.addThisPoint(event.x,event.y)

	def addThisPoint(self,x,y):
		self.canvas.create_oval(x-radius,y-radius,x+radius,y+radius)
		self.points.append([x,y])
		if len(self.points)>2:
			p1,p2=FindNearestPoints.nearestPoinst(self.points)
			self.canvas.delete('line')
			self.canvas.create_line(self.points[p1][0],self.points[p1][1],
							self.points[p2][0],self.points[p2][1],
							tags='line')

	def isToolCloseToOtherPoints(self,x,y):
		for i in range(len(self.points)):
			# pass
			if FindNearestPoints.distance(x,y, self.points[i][0], self.points[i][1])<=radius+2:
				return True
		return False

NearsestGui()