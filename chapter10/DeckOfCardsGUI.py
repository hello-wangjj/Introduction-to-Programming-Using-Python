import tkinter as tk
import random

class DeckOfCardsGUI(object):
	def __init__(self):
		super(DeckOfCardsGUI, self).__init__()

		window=tk.Tk()
		window.title('Pick Four cards randomly')

		self.imageList=[]
		for i in range(1,53):
			self.imageList.append(tk.PhotoImage(file='card/'+str(i)+'.gif'))
		frame=tk.Frame(window)
		frame.pack()

		self.labelList=[]
		for i in range(4):
			self.labelList.append(tk.Label(frame,image=self.imageList[i]))
			self.labelList[i].pack(side=tk.LEFT)

		tk.Button(window,text='Shuffle',command=self.shuffle).pack()

		window.mainloop()
	def shuffle(self):
		random.shuffle(self.imageList)
		for i in range(4):
			self.labelList[i]['image']=self.imageList[i]

DeckOfCardsGUI()