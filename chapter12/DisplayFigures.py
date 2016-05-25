import tkinter as tk
from FigureCanvas import FigureCanvas
class DisplayFigure(object):
	"""docstring for DisplayFigure"""
	def __init__(self):
		super(DisplayFigure,self).__init__()
		# self.arg = arg
		window=tk.Tk()
		window.title('Display Figure')
		
		figure1=FigureCanvas(window, 'line',width=100,height=100)
		figure1.grid(row=1,column=1)
		figure2=FigureCanvas(window, 'rectangle',False,width=100,height=100)
		figure2.grid(row=1,column=2)
		figure3=FigureCanvas(window, 'oval',False,width=100,height=100)
		figure3.grid(row=1,column=3)
		figure4=FigureCanvas(window, 'arc',False,width=100,height=100)
		figure4.grid(row=1,column=4)
		figure5=FigureCanvas(window, 'rectangle',True,width=100,height=100)
		figure5.grid(row=1,column=5)
		figure6=FigureCanvas(window, 'oval',True,width=100,height=100)
		figure6.grid(row=1,column=6)
		figure7=FigureCanvas(window, 'arc',True,width=100,height=100)
		figure7.grid(row=1,column=7)

		window.mainloop()

if __name__=='__main__':
	DisplayFigure()