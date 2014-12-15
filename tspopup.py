from Tkinter import *

class transcriptPopup:
	def __init__(self, master, transcript):
		self.root=master
		self.root.geometry('300x200')
		frame=Frame(master)
		frame.config(bg="white")
		frame.pack()
		tscr=Message(self.root, text=transcript)
		tscr.pack(anchor=W, side=LEFT, expand=1, fill=BOTH) #and it STILL refuses to stick left.
		tscr.bind("<Configure>", lambda e: tscr.configure(width=e.width-10))