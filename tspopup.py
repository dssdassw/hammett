from Tkinter import *
import func

class transcriptPopup:
	def __init__(self, master, transcript):
		self.root=master
		frame=Frame(master)
		frame.config(bg="white")
		frame.pack()
		tscr=Message(self.root, text=[item for item in func.processInput(transcript)])