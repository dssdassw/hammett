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

def createFourBttn(proofs):
	fbttn=fourBttn(Toplevel(root), proofs)
	pass
def createListPopup(inlist):
	lpopup=listPopup(Toplevel(root), inlist)
def createTranscriptPopup(transcript): #if I'm gonna do a transcript thing, I should have a print function which adds stuff to the transcript log too.
	tpopup=transcriptPopup(Toplevel(root), transcript) the transcript log too.
	pass
def updateStory(message, transcript=ts):
	smsg.set(message)
	transcript+=(message+'\n')
	return transcript
def nextMessage(script, proofs, transcript, i, root=root): # i=the index. It's a pointer.
	if script[i.get()]=='!A':
		i.set(0)
		createFourBttn(proofs)
	else:
		updateStory(script[i.get()], transcript)
		i.set(i.get()+1)
	root.update()	
def checkIfAlive(tkObj, root): #I spent an hour dealing with stupid root.after before I read about root.update, which this uses.
	try:
		if tkObj.root.state() == 'normal':
			print "It is alive!"
			return True
		else:
			print "It's dead..."
			return False
	except:
		print "Passed object missing root, therefore the window associated with the object has been destroyed."
		return False
		print "False has been returned."
	print "Made it out!"
	root.update()
	#issues with this: any new instance of the passed object besides the default is considered nonexistent.
	#could actually be an issue with the instance, not this. This might be a tough bug to solve.

ts="Player: statement number 1\nSuspect: statement number 2\nPlayer: statement number 3\n"
TESTLIST=["Knife is victim's", "Killer entered prior to 4 PM", "Suspect's name is written in blood"]
smsg=StringVar()
smsg.set("This is a test message.")
storymsg=Message(root, textvariable=smsg)
storymsg.pack(side=BOTTOM, anchor=CENTER, fill=X, expand=1)
storymsg.bind("<Configure>", lambda e: storymsg.configure(width=e.width-10)) #I had to use a lambda here because the function that I'm calling needs an argument.
proofdisp=Button(root, text="Proofs", command=lambda: createListPopup(TESTLIST))
prooficon=PhotoImage(file="proofs.gif") #initialising the image...
proofdisp.config(image=prooficon) #configuring the button to have the image on it...
proofdisp.image=prooficon #so that the image won't get gobbled up when python garbage-collects the variable.
proofdisp.pack(anchor=NW, side=LEFT, fill=X, expand=1)  #Also, should have an image in this button instead of words.
transdisp=Button(root, text="Transcript", command=lambda: createTranscriptPopup(ts)); transicon=PhotoImage(file="transcript.gif"); transdisp.config(image=transicon); transdisp.image=transicon; transdisp.pack(anchor=N, side=LEFT, fill=X, expand=1)
debugbttn=Button(root, text="DEBUG: CREATE fourBttn", command=lambda: createFourBttn(TESTLIST)); debugicon=PhotoImage(file="debugbtn.gif"); debugbttn.config(image=debugicon); debugbttn.image=debugicon; debugbttn.pack(anchor=SW, fill=X, side=BOTTOM)
four=fourBttn(Toplevel(root), TESTLIST)
Button(root, text="Next", command=lambda: nextMessage(script, TESTLIST, ts, i)).pack(anchor=CENTER)
selection = 0

while True:
	print "Beginning loop"
	stage1=checkIfAlive(four, root)
	if stage1: #interpreted as "if stage1 == True".
		print "Window is still open"
		selection = four.vsel
	elif not stage1:
		print "Window is closed."
		ts=updateStory("The player has closed the window, the story can progress!", ts)
	root.mainloop()
	print "Passed mainloop"