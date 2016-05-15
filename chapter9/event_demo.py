import tkinter as tk
class MouseKeyEvent(object):
	def __init__(self):
		super(MouseKeyEvent, self).__init__()

		window=tk.Tk()
		window.title('mouse event doemo')
		canvas=tk.Canvas(window,bg='white',width=200,height=200)
		canvas.pack()

		canvas.bind('<Button-1>',self.processMouseEvent)

		canvas.bind('<Key>',self.processKeyEvent)
		canvas.focus_set()
		window.mainloop()


	def processMouseEvent(self,event):
		print('clicked at ',event.x,event.y)
		print('position at the screen ',event.x_root,event.y_root)
		print('which button is clicked?',event.num)

	def processKeyEvent(self,event):
		print('keysym? ',event.keysym)
		print('char? ',event.char)
		print('keycode? ',event.keycode)

MouseKeyEvent()