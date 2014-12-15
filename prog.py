from Tkinter import *
from fourbttngui import *
from listpopup import *
from tspopup import *
from pointers import *
import random

#"What do you think of this splendid tuna?"
#"I'm afraid that's an island skipjack..."
#Best quote NA. Keeping this here.

root=Tk() #creating a child class or just a class using this creates more problems than it solves. I learned that from experience.
root.title(string="Hammett")
ts="Player: statement number 1\nSuspect: statement number 2\nPlayer: statement number 3\n"
script=["This is a story ", "all about how ", "my life got flipped-turned upside-down ", "I'd like to take a minute; just sit right there, let me tell you about how I became the prince of a town called Bel-Air.", '!A'] #best script.
#'!A' is a "control character" of sorts that I'm using to tell the program when to create a four-button popup.
i=ref(0)
checkpoint=ref(False)
objReturner=ref(0)
def checkIfDone(bttnwin):
	print "bttnwin.done=",bttnwin.done
def createFourBttn(proofs, pointer, boolpointer):
	print "creating four button"
	four=fourBttn(Toplevel(root), proofs)
	four.root.state='normal'
	boolpointer.set(True)
	pointer.set(four)
	pass
def createListPopup(inlist):
	lpopup=listPopup(Toplevel(root), inlist) #The reason I don't use a pointer to return this one is because I don't actually need to do anything to it but display it.
def createTranscriptPopup(transcript):
	tpopup=transcriptPopup(Toplevel(root), transcript) #The same reasoning applies to this one.
def updateStory(message, transcript=ts):
	smsg.set(message)
	transcript+=(message+'\n')
	return transcript
def nextMessage(script, proofs, transcript, i, launchobj, boolpointer, objpointer, root=root): # i=the index. It's a pointer.
	if script[i.get()]=='!A':
		i.set(0)
		createFourBttn(proofs, objpointer, boolpointer)
	else:
		if launchobj.done==True:
			updateStory(script[i.get()], transcript)
			i.set(i.get()+1)
		else:
			print "NO."
	root.update()

ts="Player: statement number 1\nSuspect: statement number 2\nPlayer: statement number 3\n"
prooflist=["Knife is victim's", "Killer entered prior to 4 PM", "Suspect's name is written in blood"]
smsg=StringVar()
smsg.set("This is a test message.")
storymsg=Message(root, textvariable=smsg)
storymsg.pack(side=BOTTOM, anchor=CENTER, fill=X, expand=1)
storymsg.bind("<Configure>", lambda e: storymsg.configure(width=e.width-10)) #I had to use a lambda here because the function that I'm calling needs an argument.
proofdisp=Button(root, text="Proofs", command=lambda: createListPopup(prooflist))
prooficon=PhotoImage(file="proofs.gif") #initialising the image...
proofdisp.config(image=prooficon) #configuring the button to have the image on it...
proofdisp.image=prooficon #so that the image won't get gobbled up when python garbage-collects the variable.
proofdisp.pack(anchor=NW, side=LEFT, fill=X, expand=1)  #Also, should have an image in this button instead of words.
transdisp=Button(root, text="Transcript", command=lambda: createTranscriptPopup(ts)); transicon=PhotoImage(file="transcript.gif"); transdisp.config(image=transicon); transdisp.image=transicon; transdisp.pack(anchor=N, side=LEFT, fill=X, expand=1)
debugbttn=Button(root, text="DEBUG: CREATE fourBttn", command=lambda: createFourBttn(prooflist, objReturner, checkpoint)); debugicon=PhotoImage(file="debugbtn.gif"); debugbttn.config(image=debugicon); debugbttn.image=debugicon; debugbttn.pack(anchor=SW, fill=X, side=BOTTOM)
four=fourBttn(Toplevel(root), prooflist)
four.done=True #because I haven't launched asked anything yet, it's "done".
Button(root, text=("Next"), command=lambda: nextMessage(script, prooflist, ts, i, four, checkpoint, objReturner)).pack(anchor=CENTER)
cproof = 0 #cproof is the ChoiceProof, or the proof provided for the choice. It's an index corresponding to the pressed putton. For example, if the user selected the first option, this would be 0.
abcd = 0 #index of the user's choice for choice a, b, c, or d. a = 0, b = 0, and so on.
print "Ignore console output unless you are a developer!"

while True:
	print 'mainloop {'
	root.mainloop()
	print abcd,':',cproof
	if checkpoint.get():
		checkpoint.set(False)
		four=objReturner.get()
	cproof=four.vsel
	abcd=four.opt.get() #if something breaks, put these before checking if checkpoint.get returns True
	checkIfDone(four)
	print '}'