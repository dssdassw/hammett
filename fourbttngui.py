from Tkinter import *

class fourBttn:
	def __init__(self, master, proofs): #after I created the twoBttn, I realized it would probably have been better to have the proof selection as a seperate window, but at the time, I didn't know I'd decide to make a similar window with only 2 choices.
		self.root=master
		frame = Frame(self.root)
		frame.pack()
		self.v = IntVar()
		self.vsel = 0
		self.opt = IntVar()
		self.info = proofs
		self.done = False
		self.closed = False
		self.imposter = False #Fugliest workaround NA.
		self.root.protocol("WM_DELETE_WINDOW", self.callback) #When the even WM_DELETE_WINDOW occurs, this protocall is executed. WM_DELETE_WINDOW is obviously when the window manager, be it X, Windows, whatever, attempts to close the window.
		customblu='#%02x%02x%02x' % (27,60,191) #A little trick to get custom colors to work.
		customgre='#%02x%02x%02x' % (26,181,81)
		customyel='#%02x%02x%02x' % (245,241,17)
		customred='#%02x%02x%02x' % (227,39,39)
		self.a = Button(self.root, text="Option A", bg=customblu, fg="white", command=lambda:self.proofmenutransition(0)); del customblu
		self.b = Button(self.root, text="Option B", bg=customgre, fg="black", command=lambda:self.proofmenutransition(1)); del customgre
		self.c = Button(self.root, text="Option C", bg=customyel, fg="black", command=lambda:self.proofmenutransition(2)); del customyel
		self.d = Button(self.root, text="Option D", bg=customred, fg="white", command=lambda:self.proofmenutransition(3)); del customred
		self.a.pack(side=LEFT, expand=1, fill=BOTH)
		self.b.pack(side=LEFT, expand=1, fill=BOTH)
		self.c.pack(side=LEFT, expand=1, fill=BOTH)
		self.d.pack(side=LEFT, expand=1, fill=BOTH)
	def callback(self): #actually LETS you close the stupid window. The values will be reset in __init__ when it is recreated, which I want.
		self.closed=True
		self.root.quit()
		self.root.destroy()
	def setvar(self): #sets the variables that inform the outside world that it is compelte, and what values it got.
		self.vsel=self.v.get()
		self.done=True
		self.root.quit()
		print "	vsel: " + str(self.vsel)
	def proofmenu(self):
		customcolor='#%02x%02x%02x' % (200,50,50)
		Button(self.root, text="Back", bg=customcolor, fg="white", command=self.remember4).pack(side=TOP, padx=25,fill=X); del customcolor
		print "	info: " + str(self.info)
		for item in self.info:
			a = Radiobutton(self.root, text=item, variable=self.v, value=self.info.index(item), command=self.setvar) #the text is the name of the item, each button puts output (I THINK) intanchoring W (so that they dont each get tabbed).
			a.pack(anchor=W)
		exitmsg=Message(self.root, text="After you've made your selection, it is safe to close this window via the X.")
		"""
		Regarding "After you've made your selection, it is safe to close this window via the X"...
		If I don't do it this way, Tkinter decides to fail at returning the value for some reason, (and by 'fail', I mean not setting the variables to anything but 0 for... some reason. Instead,
		the way I managed to was using a variable which the main window is always checking as long as I haven't destroyed this window.
		I let the main window know this one has been destroyed (without using the messy and often broken root.state, which doesn't think instances of a class are still valid) by
		using the self.root.protocol("WM_DELETE_WINDOW", self.callback) defined in the __init__ to call a callback when the window is closed that sets the variable self.closed to True.
		Just because the user closed the window doesn't mean that they actually completed the forms though, and I was wary of that.
		There is another variable, self.done, which is set to True when the user has selected a proof (and therefore is now done). I usually don't like using variables unless I actually have to, but in this case it was better to use them then to not.
		"""
		exitmsg.pack(anchor=S, fill=X, expand=1)
		exitmsg.bind("<Configure>", lambda e: exitmsg.configure(width=e.width-10)) #this is to make the message fill the window width, even when it expands. Don't know why Tkinter doesn't have a function like this built into Message, but whatever.
	def forget4(self): #"forgets" the four choices, but keeps them in memory just in case they need to be recalled. It's as close as Tkinter gets to deleting them.
		self.a.pack_forget()
		self.b.pack_forget()
		self.c.pack_forget()
		self.d.pack_forget()
	def remember4(self): #performs "back" action, removing everything on the window and "remembering" the four choices.
		for widget in self.root.pack_slaves():
			widget.pack_forget()
		self.a.pack(side=LEFT)
		self.b.pack(side=LEFT)
		self.c.pack(side=LEFT)
		self.d.pack(side=LEFT)
	def proofmenutransition(self, sel): #sets up for the proof menu, then calls it.
		self.forget4()
		self.opt.set(sel)
		print '	four.opt =',self.opt.get()
		self.proofmenu()
		print '	v 1: ' + str(self.v)
		return 0