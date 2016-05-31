import urllib.request
import tkinter as tk
import tkinter.messagebox

def showResult():
	# pass
	counts=analyzeFile(url.get())
	text.delete(0.0,tk.END)
	for i in range(len(counts)):
		text.insert(tk.END,chr(ord('a')+i)+' appears '+
					str(counts[i])+(' time' if counts[i]<2 else ' times')+'\n')

def analyzeFile(url):
	try:
		infile=urllib.request.urlopen(url)
		s=str(infile.read().decode())
		counts=countLetters(s.lower())
		return counts
	except ValueError:
		tkinter.messagebox.showwarning('Analyze Url','URL:'+
							url+'does not exist')



def countLetters(s):
	counts=26*[0]
	for ch in s:
		if ch.isalpha():
			counts[ord(ch)-ord('a')]+=1
	return counts



window=tk.Tk()
window.title('Occurence of letters from URL')

frame1=tk.Frame(window)
frame1.pack()
scrollBar=tk.Scrollbar(frame1)
scrollBar.pack(side=tk.RIGHT,fill=tk.Y)
text=tk.Text(frame1,width=60,height=10,wrap=tk.WORD,yscrollcommand=scrollBar.set)
text.pack()
scrollBar.config(command=text.yview)

frame2=tk.Frame(window)
frame2.pack()
tk.Label(frame2,text='Enter a url: ').pack(side=tk.LEFT)
url=tk.StringVar()
tk.Entry(frame2,textvariable=url).pack(side=tk.LEFT)
tk.Button(frame2,text='Show Result',command=showResult).pack(side=tk.LEFT)

window.mainloop()