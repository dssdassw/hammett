from Tkinter import *
from fourbttngui import *
from listpopup import *
from tspopup import *
import random

def createFourBttn(proofs):
	fbttn=fourBttn(Toplevel(root), proofs)
	pass
def createListPopup(inlist):
	lpopup=listPopup(Toplevel(root), inlist)
def createTranscriptPopup(transcript): #if I'm gonna do a transcript thing, I should have a print function which adds stuff to the transcript log too.
	tpopup=transcriptPopup(Toplevel(root), transcript)
	pass
def updateStory(message, transcript):
	smsg.set(message)
	transcript+=(message+'\n')
	return transcript

ts="Player: statement number 1\nSuspect: statement number 2\nPlayer: statement number 3\n"
TESTLIST=["Knife is victim's", "Killer entered prior to 4 PM", "Suspect's name is written in blood"]
root=Tk() #creating a child class or just a class using this creates more problems than it solves. I learned that from experience.
smsg=StringVar()
smsg.set("This is a test message.")
storymsg=Message(root, textvariable=smsg)
storymsg.pack(side=BOTTOM, anchor=CENTER, fill=X, expand=1)
storymsg.bind("<Configure>", lambda e: storymsg.configure(width=e.width-10)) #I had to use a lambda here because the function I'm calling needs an argument.
Button(root, text="Proofs", command=lambda: createListPopup(TESTLIST)).pack(side=TOP, anchor=NW, expand=1)  #Also, should have an image in this button instead of words.
Button(root, text="Transcript", command=lambda: createTranscriptPopup(ts)).pack(side=TOP, anchor=NW, expand=1)
Button(root, text="DEBUG: CREATE fourBttn", command=lambda: createFourBttn(TESTLIST)).pack(side=BOTTOM)
four=fourBttn(Toplevel(root), TESTLIST)
selection = 0
c=0
done=False
while True:
	selection=four.vsel
	c+=1
	ts=updateStory("This is test message #"+str(c)+".\nThe player has selected option #"+str(selection)+".", ts) #works nicely!
	#add some code that checks if the window is still open, though, to prevent the player from just selecting
	#random checkboxes in the list to progress the story without actually doing anything.
	root.mainloop()
	done=True