from Tkinter import *

class listPopup:
	def __init__(self, master, prooflist):
		self.root=master
		frame=Frame(self.root)
		frame.pack()
		ysb = Scrollbar(self.root, orient=VERTICAL)
		xsb = Scrollbar(self.root, orient=HORIZONTAL)
		lb = Listbox(self.root, yscrollcommand=ysb.set, xscrollcommand=xsb.set)
		for proof in prooflist:
			lb.insert(END, proof)
		ysb.config(command=lb.yview)
		xsb.config(command=lb.xview)
		ysb.pack(side=RIGHT, anchor=E, fill=Y, expand=1)
		xsb.pack(side=BOTTOM, anchor=S, fill=X, expand=1)
		lb.pack(side=LEFT, fill=BOTH, expand=1)
			