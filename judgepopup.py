from Tkinter import *

class judgePopup:
	def __init__(self, master, correctcombo, inputcombo, correctText, incorrectText):
		self.root=master
		self.root.geometry('300x200')
		frame=Frame(master)
		if correctcombo == inputcombo:
			self.root.title("CORRECT!")
			text=Message(self.root, text=correctText)
			self.result=True
		else:
			self.root.title("INCORRECT!")
			text=Message(self.root, text=incorrectText)
			self.result=False
		frame.pack()
		text.pack(anchor=W, side=LEFT, fill=BOTH, expand=1)
		text.bind("<Configure>", lambda e: text.configure(width=e.width-10))