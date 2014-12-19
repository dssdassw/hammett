from Tkinter import *

class listPopup:
	def __init__(self, master, prooflist):
		self.root=master
		self.root.geometry('500x500')
		frame=Frame(self.root)
		ysb = Scrollbar(self.root, orient=VERTICAL)
		lb = Listbox(self.root, yscrollcommand=ysb.set)
		for proof in prooflist:
			print "	inserting '" + proof + "' into the listbox."
			lb.insert(END, proof)
		ysb.config(command=lb.yview)
		lb.pack(side=LEFT, fill=BOTH, expand=1)
		ysb.pack(anchor=E, fill=Y, expand=1)
		frame.pack()