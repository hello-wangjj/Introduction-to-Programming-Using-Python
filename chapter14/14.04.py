from tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import askopenfilename

window=tk.Tk()
window.title('Occurence of Letters')

frame1=tk.Frame(window)
frame1.pack()

scrollBar=tk.Scrollbar(frame1)
scrollBar.pack(side=tk.RIGHT,fill=tk.Y)
text=tk.Text(frame1,width=40,height=10,wrap=tk.WORD,yscrollcommand=scrollBar.set)
text.pack()

frame2=tk.Frame(window)
frame2.pack()

tk.Label(frame2,text='enter a file name: ').pack(side=tk.LEFT)
