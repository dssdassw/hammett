from Tkinter import *

class twoBttn:
	def __init__(self, master, proofs):
		self.root=master
		frame = Frame(self.root)
		frame.pack()
		self.v = IntVar()
		self.vsel = 0
		self.opt = IntVar()
		self.info = proofs
		self.done = False
		self.closed = False
		self.imposter = False
		self.root.protocol("WM_DELETE_WINDOW", self.callback)
		customred='#%02x%02x%02x' % (227,39,39)
		customgre='#%02x%02x%02x' % (26,181,81)
		self.f = Button(self.root, text="No", bg=customred, fg="white", command=lambda:self.proofmenutransition(0)); del customred
		self.t = Button(self.root, text="Yes", bg=customgre, fg="black", command=lambda:self.proofmenutransition(1)); del customgre
		self.t.pack(side=LEFT, expand=1, fill=BOTH)
		self.f.pack(side=LEFT, expand=1, fill=BOTH)
	def callback(self):
		self.closed=True
		self.root.quit()
		self.root.destroy()
	def setvar(self):
		self.vsel=self.v.get()
		self.done=True
		self.root.quit()
		print "	vsel: " + str(self.vsel)
	def proofmenu(self):
		customcolor='#%02x%02x%02x' % (200,50,50)
		Button(self.root, text="Back", bg=customcolor, fg="white", command=self.remember2).pack(side=TOP, padx=25,fill=X); del customcolor
		print "	info: " + str(self.info)
		for item in self.info:
			a = Radiobutton(self.root, text=item, variable=self.v, value=self.info.index(item), command=self.setvar)
			a.pack(anchor=W)
		exitmsg=Message(self.root, text="After you've made your selection, it is safe to close this window via the X.")
		exitmsg.pack(anchor=S, fill=X, expand=1)
		exitmsg.bind("<Configure>", lambda e: exitmsg.configure(width=e.width-10))
	def forget2(self):
		self.t.pack_forget()
		self.f.pack_forget()
	def remember2(self):
		for widget in self.root.pack_slaves():
			widget.pack_forget()
		self.t.pack(side=LEFT)
		self.f.pack(side=LEFT)
	def proofmenutransition(self, sel):
		self.forget2()
		self.opt.set(sel)
		print '	two.opt =',self.opt.get()
		self.proofmenu()
		print '	v 1: ' + str(self.v)
		return 0