from Tkinter import *
from fourbttngui import *
from listpopup import *
from tspopup import *
import random

#"What do you think of this splendid tuna?"
#"I'm afraid that's an island skipjack..."
root=Tk() #creating a child class or just a class using this creates more problems than it solves. I learned that from experience.
ts="Player: statement number 1\nSuspect: statement number 2\nPlayer: statement number 3\n"
def createFourBttn(proofs):
	fbttn=fourBttn(Toplevel(root), proofs)
	pass
def createListPopup(inlist):
	lpopup=listPopup(Toplevel(root), inlist)
def createTranscriptPopup(transcript): #if I'm gonna do a transcript thing, I should have a print function which adds stuff to the transcript log too.
	tpopup=transcriptPopup(Toplevel(root), transcript)
	pass
def updateStory(message, transcript=ts):
	smsg.set(message)
	transcript+=(message+'\n')
	return transcript
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

#Note: could I put all the lines of a story into a list and just go over them?
ts="Player: statement number 1\nSuspect: statement number 2\nPlayer: statement number 3\n"
TESTLIST=["Knife is victim's", "Killer entered prior to 4 PM", "Suspect's name is written in blood"]
smsg=StringVar()
smsg.set("This is a test message.")
storymsg=Message(root, textvariable=smsg)
storymsg.pack(side=BOTTOM, anchor=CENTER, fill=X, expand=1)
storymsg.bind("<Configure>", lambda e: storymsg.configure(width=e.width-10)) #I had to use a lambda here because the function I'm calling needs an argument.
proofdisp=Button(root, text="Proofs", command=lambda: createListPopup(TESTLIST))
prooficon=PhotoImage(file="es2.gif")
proofdisp.config(image=prooficon)
proofdisp.image=prooficon #so that the image won't get gobbled up when python garbage-collects the variable.
proofdisp.pack(anchor=NW, side=LEFT, fill=X, expand=1)  #Also, should have an image in this button instead of words.
Button(root, text="Transcript", command=lambda: createTranscriptPopup(ts)).pack(anchor=N, side=LEFT, fill=X, expand=1)
Button(root, text="DEBUG: CREATE fourBttn", command=lambda: createFourBttn(TESTLIST)).pack(anchor=SW, fill=X, side=BOTTOM)
four=fourBttn(Toplevel(root), TESTLIST)
selection = 0
c=0
while True:
	c+=1
	print "Beginning loop"
	stage1=checkIfAlive(four, root)
	ts=updateStory("This is test message #"+str(c)+".\nThe player has selected option #"+str(selection)+".", ts)
	if stage1: #interpreted as "if stage1 == True".
		print "Window is still open"
		selection = four.vsel
	elif not stage1:
		print "Window is closed."
		ts=updateStory("The player has closed the window, the story can progress!", ts)
	root.mainloop()
	print "Passed mainloop"