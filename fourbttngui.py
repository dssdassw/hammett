from Tkinter import *

class fourBttn:
	def __init__(self, master, proofs):
		self.root=master
		frame = Frame(self.root)
		frame.pack()
		self.v = IntVar()
		self.vsel = 0
		self.info = proofs
		customblu='#%02x%02x%02x' % (27,60,191)#A little trick to get custom colors to work.
		customgre='#%02x%02x%02x' % (26,181,81)
		customyel='#%02x%02x%02x' % (245,241,17)
		customred='#%02x%02x%02x' % (227,39,39) 
		self.a = Button(self.root, text="Option A", bg=customblu, fg="white", command=self.proofmenutransition); del customblu
		self.b = Button(self.root, text="Option B", bg=customgre, fg="black", command=self.proofmenutransition); del customgre
		self.c = Button(self.root, text="Option C", bg=customyel, fg="black", command=self.proofmenutransition); del customyel
		self.d = Button(self.root, text="Option D", bg=customred, fg="white", command=self.proofmenutransition); del customred
		self.a.pack(side=LEFT, expand=1, fill=BOTH)
		self.b.pack(side=LEFT, expand=1, fill=BOTH)
		self.c.pack(side=LEFT, expand=1, fill=BOTH)
		self.d.pack(side=LEFT, expand=1, fill=BOTH)
	def seta(self):
		self.vsel=self.v.get()
		self.root.quit()
		print self.vsel
	def proofmenu(self):
		print self.info
		customcolor='#%02x%02x%02x' % (200,50,50)
		Button(self.root, text="Back", bg=customcolor, fg="white", command=self.remember4).pack(side=TOP, padx=25,fill=X); del customcolor
		self.info=[(item, self.info.index(item)) for item in self.info] #returns the tuple (item, self.info.index(item)) for each item in the list self.info.
		print self.info
		for item, index in self.info:
			a = Radiobutton(self.root, text=item, variable=self.v, value=index, command=self.seta) #the text is the name of the item, each button puts output (I THINK) intanchoring W (so that they dont each get tabbed). 
			a.pack(anchor=W)
		exitmsg=Message(self.root, text="After you've made your selection, it is safe to close this window via the X.")
		exitmsg.pack(anchor=S, fill=X, expand=1)
		exitmsg.bind("<Configure>", lambda e: exitmsg.configure(width=e.width-10)) #this is to make the message fill the window width, even when it expands. Don't know why Tkinter doesn't have a function like this built into Message, but whatever.
	def forget4(self):
		self.a.pack_forget()
		self.b.pack_forget()
		self.c.pack_forget()
		self.d.pack_forget()
	def remember4(self):
		for widget in self.root.pack_slaves():
			widget.pack_forget()
		self.a.pack(side=LEFT)
		self.b.pack(side=LEFT)
		self.c.pack(side=LEFT)
		self.d.pack(side=LEFT)
	def proofmenutransition(self):
		self.forget4()
		self.proofmenu()
		print self.v
		return 0