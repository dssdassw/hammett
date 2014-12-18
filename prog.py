from Tkinter import *
from fourbttngui import *
from listpopup import *
from tspopup import *
from pointers import *
from fakeWindow import * #an unfortunate hack that was necessary: a object containing only the element "self.done" to trick the program into launching and initializing four without breaking or actually popping up four.
from judgepopup import *
import random

#"What do you think of this splendid tuna?"
#"I'm afraid that's an island skipjack..."
#Best quote NA. Keeping this here.

root=Tk() #creating a child class or just a class using this creates more problems than it solves. I learned that from experience.
root.geometry('200x500') #process that sets the dimentions (for some reason referred to as the geometry) of the window.
root.title(string="Hammett") #pretty self-explainatory. Sets the title of the root window.
ts=ref("") #A pointer, pointing to the transcript. I had to use pointers (created with the "ref" class) for a lot of things, as Tk doesn't return values.
script=["This is a logic game. You'll start out with some basic information, which you can check via the 'PROOFS' button above.", 
"You can also check everything that has been said recently via the 'TRANSCRIPT' button above.", "Now, let's get to the story.", "A murder was committed at a home in Wyoming.", 
"The police have narrowed their search to 4 possible culprits.", "You and a detective named John will be speaking with each of them.", "The police have already told you everything they know. Here it is:",
"The victim's name is Zack, and the other three suspects are Aaron, Ben, Charlie and Derrick.", "You've yet to actually see any of them.", "The murder was committed in Zack's home.",
"Zack died at approximately 4:00 PM on December 14, 2014, due blood loss.",  "The murder weapon was Derrick's pocket knife.", "Derrick was found unconscious at the scene of the crime.", 
"Ben was the first to discover the crime scene.", "Charlie was confirmed to be on a flight back to Toronto from 2:00 PM to 6:00 PM on the 14th of December.",
"...And that's it. The first suspect you and John will be speaking to is Charlie.", "You suspect that the police want to see if you are actually up to the task of helping with the investigation.",
"(Dramatic fade to black)", "You're sitting in the interview room, talking with John about the case, when suddenly, an officer outside the door announces that the suspect will be entering the room.",
"Charlie enters the room with a look of apprehension, hands uncomfortably wriggling in his handcuffs. He's obviously nervous.", "Charlie: '...do you really think I did it? What kind of third-rate detective--'",
"John: 'Easy there. Just tell us--'", "Charlie: 'I don't know anything!!!'",
"John, looking slightly annoyed, glances at you, but doens't lose his composure. He probably wants you to say something. You don't, because you have certain tropes to fill.",
"John: 'Listen, Charlie, we don't think you did it. It's just that the media would be pissed if we didn't pursue every single bit of info we have.'", "This seems to calm him down a little.",
"John: 'Just tell us all you know.'", "Charlie's eyes narrow a bit, but he starts.", "Charlie: 'I know that Zack was going to have a little family get-together with his siblings, something about his inheritance.'",
"John: 'Clarify. Who are his siblings?'", "Charlie: 'You honestly don't know that yet?'", "John: 'I do. My friend here doesn't.'",
"You feel out of place. For a second you also wonder why John doesn't just tell you directly. Then you get it. You don't say anything about John's third-rate detective work, and hope John doesn't notice you stifling a laugh.",
"Charlie: 'Oh. Well Aaron, Ben, and Zack are brothers, Zack being the oldest, and Ben being the youngest.'", '!A'] #more please.

prooflist=["Crime scene was victim's home", "Victim died due to blood loss", "Victim died at about 4:00 PM", "Murder weapon was Derrick's pocket knife", "Ben discovered the crime scene", "Charlie was on a flight from 2:00PM to 6:00PM"]
#'!A' is a "control character" of sorts that I'm using to tell the program when to create a four-button popup.
i=ref(0) #the iterating variable I made a pointer because the process that uses it is called only by a button, which doesn't collect return values. You can GIVE it arguments via an unbound function (lambda), but you can't store the returned values anywhere because of where you define the call.
checkpoint=ref(False) #had to be made a pointer for the same reason as the pointer above.
objReturner=ref(0) #A pointer storing the fourBttn window I want to return. For various reasons this couldn't be stored, so I had to do this.
twistID=0 #finally, a variable that ISN'T a pointer...

def checkIfDone(bttnwin, proofs, new_info, twistID): #Checks if the window's forms are completed, that the window has been closed, and that it isn't actually just a fake window (which is a nasty workaround I had to use.) If this is the case, this function also performs completion actions and is the only def here that defines a function, not a process.
	if bttnwin.done and bttnwin.closed and not bttnwin.imposter:
		if new_info not in proofs: #otherwise an indecisive player will find that their proof list has multiples of the same piece of info on it because they clicked a bunch of the boxes for no reason or something.
			proofs.append(new_info)
			twistID+=1
	else:
		print "	The task is incomplete. (bttnwin.done and bttnwin.closed and not bttnwin.imposter evaluates to False.)"
	return twistID #note that I don't have to return proofs. This is because proofs will be a list, therefore it is pretty much a collection of pointers pointing to data.

def createFourBttn(proofs, pointer, boolpointer): #This process, as aptly explained via the name, creates a four-button window. It also sets the window's root.state to normal to show that it is fully operational, and "returns" the new instance of fourBttn called four by using two pointers.
	#...Specifically, it sets boolpointer to True (boolpointer tells the main window to set the value of four to whatever is stored in pointer (which, to the outside world, is known as objReturner)), and sets pointer (which is objReturner) to the new instance of fourBttn it has created.
	print "	Creating a four button..."
	four=fourBttn(Toplevel(root), proofs)
	four.done=False; four.closed=False
	four.root.state='normal'
	boolpointer.set(True)
	pointer.set(four)

def createListPopup(inlist):
	lpopup=listPopup(Toplevel(root), inlist) #The reason I don't use a pointer to return this one is because I don't actually need to do anything to it but display it.

def createTranscriptPopup(transcript):
	tpopup=transcriptPopup(Toplevel(root), transcript) #The same reasoning applies to this one.

def updateStory(message, transcript=ts):
	smsg.set(message)
	transcript.set(transcript.get()+message+'\n')

def nextMessage(script, proofs, transcript, i, launchobj, boolpointer, objpointer, root=root): #i=the index. It's a pointer.
	if script[i.get()]=='!A':
		i.set(0)
		launchobj.done=False
		launchobj.closed=False
		createFourBttn(proofs, objpointer, boolpointer)
	else:
		if launchobj.done and launchobj.closed:
			updateStory(script[i.get()], transcript) #the order is the reverse of the above outcome, because here I want it to show where the message currently is without skipping over something.
			i.set(i.get()+1)
		else:
			createFourBttn(proofs, objpointer, boolpointer)
	root.update()

def conlb(number): #cosole line break. Just wanted a way to type it faster without keeping it in my clipboard.
	print "Task #",number," has been completed.\n------------------------\n\n"

smsg=StringVar()
smsg.set("Welcome to Hammett! Press the 'NEXT' button above to continue.")
storymsg=Message(root, textvariable=smsg)
storymsg.pack(side=BOTTOM, anchor=CENTER, fill=X, expand=1)
storymsg.bind("<Configure>", lambda e: storymsg.configure(width=e.width-10)) #I had to use a lambda here because the function that I'm calling needs an argument.
proofdisp=Button(root, text="Proofs", command=lambda: createListPopup(prooflist))
prooficon=PhotoImage(file="proofs.gif") #initialising the image
proofdisp.config(image=prooficon) #configuring the button to have the image on it
proofdisp.image=prooficon #saving the image in a class so that the image won't get gobbled up when python garbage-collects the variable.
proofdisp.pack(anchor=NW, side=LEFT, fill=X, expand=1)  #Also, should have an image in this button instead of words.
transdisp=Button(root, text="Transcript", command=lambda: createTranscriptPopup(ts.get()))
transicon=PhotoImage(file="transcript.gif")
transdisp.config(image=transicon)
transdisp.image=transicon
transdisp.pack(anchor=N, side=LEFT, fill=X, expand=1)
four=fakewin()
nextbttn=Button(root, text=("Next"), command=lambda: nextMessage(script, prooflist, ts, i, four, checkpoint, objReturner))
nexticon=PhotoImage(file="next-arrow.gif")
nextbttn.config(image=nexticon)
nextbttn.image=nexticon
nextbttn.pack(anchor=CENTER)
cproof = 0 #cproof is the ChoiceProof, or the proof provided for the choice. It's an index corresponding to the pressed putton. For example, if the user selected the first option, this would be 0.
abcd = 0 #index of the user's choice for choice a, b, c, or d. a = 0, b = 0, and so on.
cproof2 = 0
abcd2 = 0
print "Ignore console output unless you are a developer!"

while twistID==0:
	print 'mainloop {'
	root.mainloop()
	print '	',abcd,':',cproof
	if checkpoint.get():
		checkpoint.set(False)
		four=objReturner.get()
	cproof=four.vsel
	abcd=four.opt.get() #if something breaks, put these before checking if checkpoint.get returns True
	twistID=checkIfDone(four, prooflist, "This guy truly is the fresh prince of Bel-Air", twistID)
	print '}'
conlb(twistID)
twist1=judgePopup(Toplevel(root), (0, 2), (abcd, cproof), "DAMN STRAIGHT SON", "If he wasn't the fresh prince of Bel-Air, why would he be drinking orange juice out of a champagne glass?\nFurthermore, ONLY the fresh prince would tell a cabbie that he would smell him later.\nUnless that cabbie was 2sexy4hisShirt.\nFinally, it can't be the last option because you clearly ARE an idiot.")
#twist1.result produces True if the player was correct, and False if they were incorrect.
script=["In west Philedelphia, born and raised, ", "on the playground is where I spent most of my days", '!A']

while twistID==1:
	print 'mainloop2 {'
	root.mainloop()
	print '	',abcd2,':',cproof2 #the '	' is just for formatting purposes.
	if checkpoint.get():
		checkpoint.set(False)
		four=objReturner.get()
	cproof2=four.vsel
	abcd2=four.opt.get()
	twistID=checkIfDone(four, prooflist, "The prince of Bel-Air is really Flava Flav", twistID)
	print '}'
conlb(twistID)
twist2=judgePopup(Toplevel(root), (1,0), (abcd2, cproof2), "YOU'RE GODDAMN RIGHT", "lolno")
root.mainloop()
print "- FIN -"