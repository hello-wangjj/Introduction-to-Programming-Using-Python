from tkinter import Canvas
import tkinter as tk
class FigureCanvas(Canvas):
	"""docstring for FigureCanvas"""
	def __init__(self, container,figureType,filled=False,width=100,height=100):
		#调用父类的初始化方法__init__()
		super(FigureCanvas, self).__init__(container,width=width,height=height)
		# self.arg = arg
		self.__figuredType=figureType
		self.__filled=filled
		self.drawFigure()


	def getFigureType(self):
		return self.__figuredType

	def getFilled(self):
		return self.__filled
	def setFigureType(self,type):
		self.__figuredType=type
		self.drawFigure()
	def setFilled(self,fill):
		self.__filled=fill
		self.drawFigure()


	def drawFigure(self):
		if self.__figuredType=='line':
			self.line()
		elif self.__figuredType=='rectangle':
			self.rectangle()
		elif self.__figuredType=='oval':
			self.oval()
		elif self.__figuredType=='arc':
			self.arc()


	def line(self):
		width=int(self['width'])
		height=int(self['height'])
		self.create_line(10,10,width-10,height-10)
		self.create_line(width-10,10,10,height-10)

	def rectangle(self):
		width=int(self['width'])
		height=int(self['height'])
		if self.__filled:
			self.create_rectangle(10,10,width-10,height-10,fill='red')
		else :
			self.create_rectangle(10,10,width-10,height-10)


	def oval(self):
		width=int(self['width'])
		height=int(self['height'])
		if self.__filled:
			self.create_oval(10,10,width-10,height-10,fill='red')
		else :
			self.create_oval(10,10,width-10,height-10)


	def arc(self):
		width=int(self['width'])
		height=int(self['height'])
		if self.__filled:
			self.create_arc(10,10,width-10,height-10,start=0,extent=145,fill='red')
		else :
			self.create_arc(10,10,width-10,height-10,start=0,extent=145)

if __name__=='__main__':
	window=tk.Tk()
	window.title('Display Figures')
	a=FigureCanvas(window, 'line')
	a.pack()
	window.mainloop()