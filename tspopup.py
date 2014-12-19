from Tkinter import *

class transcriptPopup:
	def __init__(self, master, transcript):
		self.root=master
		self.root.geometry('300x700')
		frame=Frame(self.root)
		tscr=Text(self.root)
		tscr.insert(END, transcript)
		ysb=Scrollbar(self.root, command=tscr.yview)
		tscr.configure(yscrollcommand=ysb.set, state=DISABLED, width=self.root.winfo_width()-10000) #The width argument is a fix for the text box taking up so much of the window that you had to resize the window to see the scrollbar. ...
		tscr.pack(fill=BOTH, side=LEFT, expand=1) # (cont'd) I wanted to keep the window's default width the same, plus have the scrollbar be easily visible at any width. 10000 seems like a magic number, and I'm pretty sure it actually is magic. ...
		tscr.bind("<Configure>", lambda e: tscr.configure(width=self.root.winfo_width()-10000)) # (cont'd) I honestly have no idea why 10000 works when it  really just should break the window. It raises no errors, and the scrollbar tracks properly.
		ysb.pack(anchor=E, fill=Y, expand=1)
		frame.pack()