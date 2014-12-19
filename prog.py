from Tkinter import *
from fourbttngui import *
from tfbttn import *
from listpopup import *
from tspopup import *
from pointers import *
from fakeWindow import * #an unfortunate hack that was necessary: an object containing the elements "self.done", "self.closed", and "self.imposter", all True, to trick the program into launching and initializing four without breaking or actually popping up four.
from judgepopup import *
import random

#"What do you think of this splendid tuna?"
#"I'm afraid that's an island skipjack..."
#Best quote NA. Keeping this here.

root=Tk() #creating a child class or just a class using this creates more problems than it solves. I learned that from experience.
root.geometry('200x500') #process that sets the dimentions (for some reason referred to as the geometry) of the window.
root.title(string="Hammett") #root.title is pretty self-explainatory. It sets the title of the root window.
ts=ref("") #A pointer, pointing to the transcript. I had to use pointers (created with the "ref" class) for a lot of things, as Tk doesn't return values.
script=["This is a logic game. You'll start out with some basic information, which you can check via the 'PROOFS' button above.",
"You can also check everything that has been said recently via the 'TRANSCRIPT' button above.", "Now, let's get to the story.", "A murder was committed at a dorm in Wyoming.",
"The police have narrowed their search to 4 possible culprits.", "You and a detective named Richard will be speaking with each of them.", "The police have already told you everything they know. Here it is:",
"The victim's name is Zack, and the other three suspects are Aaron, Ben, Charlie and Derrick.", "You've yet to actually see any of them.", "The murder was committed in Zack's dorm.",
"Zack died at approximately 4:00 PM on December 14, 2014, due blood loss.",  "The murder weapon was Derrick's pocket knife.", "Derrick was found unconscious at the scene of the crime.",
"Ben was the first to discover the crime scene.", "Charlie was confirmed to be on a flight back to Toronto from 2:00 PM to 6:00 PM on the 14th of December.",
"...And that's it. The first suspect you and Richard will be speaking to is Charlie.", "You suspect that the police want to see if you are actually up to the task of helping with the investigation.",
"(Dramatic fade to black)", "You're sitting in the interview room, talking with Richard about the case, when suddenly, an officer outside the door announces that the suspect will be entering the room.",
"Charlie enters the room with a look of apprehension, hands uncomfortably wriggling in his handcuffs. He's obviously nervous.", "Charlie: '...do you really think I did it? What kind of third-rate detective--'",
"Richard: 'Easy there. Just tell us--'", "Charlie: 'I don't know anything!!!'",
"Richard, looking slightly annoyed, glances at you, but doens't lose his composure. He probably wants you to say something. You don't, because you have certain tropes to fill.",
"Richard: 'Listen, Charlie, we don't think you did it. It's just that the media would be pissed if we didn't pursue every single bit of info we have.'", "This seems to calm him down a little.",
"Richard: 'Just tell us all you know.'", "Charlie's eyes narrow a bit, but he starts.", "Charlie: 'I know that Zack was going to have a little family get-together with his siblings. I think they knew the reason why, but nobody told me anything.'",
"Richard: 'Clarify. Who are his siblings?'", "Charlie: 'You honestly don't know that yet?'", "Richard: 'I do. My friend here doesn't.'",
"You feel out of place. For a second you also wonder why Richard doesn't just tell you directly. Then you get it. You don't say anything about Richard's third-rate detective work, and hope Richard doesn't notice you stifling a laugh.",
"Charlie: 'Oh. Well Aaron, Ben, and Zack are brothers, Zack being the oldest, and Ben being the youngest.'", "Charlie: 'That's all I have to tell you. Can you take these handcuffs off of me now?...",
"Here's the main part of the game. I'll ask you a question, and provide four options for an answer. When you click 'NEXT', a popup will appear.",
"Complete this popup by answering 'Yes' or 'No', then providing proof from the information you already know by clicking one of the options and closing the window.",
"From what you already know, is Charlie a valid suspect in the case?", '!B']
#'!A' tells the program to launch a four-button window, while '!B' tells it to launch a two-button window.
prooflist=["Crime scene was victim's dorm", "Victim died due to blood loss from a single puncture wound", "Victim died at about 4:00 PM", "Murder weapon was Derrick's pocket knife", "Ben discovered the crime scene", "Charlie was on a flight from 2:00PM to 6:00PM",
"Derrick was found unconscious at the crime scene"]
i=ref(0) #the iterating variable I made a pointer because the process that uses it is called only by a button, which doesn't collect return values. You can GIVE it arguments via an unbound function (lambda), but you can't store the returned values anywhere because of where you define the call.
checkpoint=ref(False) #had to be made a pointer for the same reason as the pointer above.
checkptype=ref(0)
objReturner=ref(fakewin()) #A pointer storing the fourBttn window I want to return. For various reasons this couldn't be stored, so I had to do this.
twistID=0 #finally, a variable that ISN'T a pointer...

def checkIfDone(bttnwin, proofs, new_info, twistID): #Checks if the window's forms are completed, that the window has been closed, and that it isn't actually just a fake window (which is a nasty workaround I had to use.) If this is the case, this function also performs completion actions and is the only def here that defines a function, not a process.
	if bttnwin.done and bttnwin.closed and not bttnwin.imposter:
		if new_info not in proofs: #otherwise an indecisive player will find that their proof list has multiples of the same piece of info on it because they clicked a bunch of the boxes for no reason or something.
			for proof in new_info:
				proofs.append(proof)
			twistID+=1
	else:
		print "	The task is incomplete. (bttnwin.done and bttnwin.closed and not bttnwin.imposter evaluates to False.)"
	return twistID #note that I don't have to return proofs. This is because proofs will be a list, therefore it is pretty much a collection of pointers pointing to data.

def createFourBttn(proofs, pointer, boolpointer, tpointer): #This process, as aptly explained via the name, creates a four-button window. It also sets the window's root.state to normal to show that it is fully operational, and "returns" the new instance of fourBttn called four by using two pointers.
	#...Specifically, it sets boolpointer to True (boolpointer tells the main window to set the value of four to whatever is stored in pointer (which, to the outside world, is known as objReturner)), and sets pointer (which is objReturner) to the new instance of fourBttn it has created.
	print "	Creating a four button..."
	four=fourBttn(Toplevel(root), proofs)
	four.done=False; four.closed=False
	four.root.state='normal'
	tpointer.set(4)
	boolpointer.set(True)
	pointer.set(four)

def createTwoBttn(proofs, pointer, boolpointer, tpointer):
	print "	Creating a two button..."
	two=twoBttn(Toplevel(root), proofs)
	two.done=False; two.closed=False
	two.root.state='normal'
	tpointer.set(2)
	boolpointer.set(True)
	pointer.set(two)

def createListPopup(inlist):
	lpopup=listPopup(Toplevel(root), inlist) #The reason I don't use a pointer to return this one is because I don't actually need to do anything to it but display it.

def createTranscriptPopup(transcript):
	tpopup=transcriptPopup(Toplevel(root), transcript) #The same reasoning applies to this one.

def updateStory(message, transcript=ts):
	smsg.set(message)
	transcript.set(transcript.get()+message+'\n')

def nextMessage(script, proofs, transcript, i, launchobj, boolpointer, objpointer, tpointer, root=root): #i=the index. It's a pointer.
	if script[i.get()]=='!A':
		i.set(0)
		launchobj.done=False
		launchobj.closed=False
		createFourBttn(proofs, objpointer, boolpointer, tpointer)
	elif script[i.get()]=='!B':
		i.set(0)
		launchobj.done=False
		launchobj.closed=False
		createTwoBttn(proofs, objpointer, boolpointer, tpointer)
	else:
		print script[i.get()]
		if launchobj.done and launchobj.closed:
			updateStory(script[i.get()], transcript) #the order is the reverse of the above outcome, because here I want it to show where the message currently is without skipping over something.
			i.set(i.get()+1)
		elif launchobj.closed and not launchobj.done:
			if tpointer.get() == 2:
				createTwoBttn(proofs, objpointer, boolpointer, tpointer)
			elif tpointer.get() == 4:
				createFourBttn(proofs, objpointer, boolpointer, tpointer)
			else: i.set(i.get()+1)
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
four=fakewin() #Did I mention that I hate this workaround?
two=fakewin()
nextbttn=Button(root, text=("Next"), command=lambda: nextMessage(script, prooflist, ts, i, objReturner.get(), checkpoint, objReturner, checkptype))
nexticon=PhotoImage(file="next-arrow.gif")
nextbttn.config(image=nexticon)
nextbttn.image=nexticon
nextbttn.pack(anchor=CENTER)
cproof = 0 #cproof is the ChoiceProof, or the proof provided for the choice. It's an index corresponding to the pressed putton. For example, if the user selected the first option, this would be 0.
abcd = 0 #index of the user's choice for choice a, b, c, or d. a = 0, b = 0, and so on.
cproof2 = 0; abcd2 = 0; cproof3 = 0; abcd3 = 0;
print "Ignore console output unless you are a developer!"
while twistID==0:
	print 'mainloop {'
	root.mainloop()
	print '	',abcd,':',cproof
	if checkpoint.get():
		checkpoint.set(False)
		two=objReturner.get()
	cproof=two.vsel
	abcd=two.opt.get() #if something breaks, put these before checking if checkpoint.get returns True
	twistID=checkIfDone(two, prooflist, ["A family gathering was to be held, & invitees knew why", "Zack was the oldest sibling", "Ben is the youngest sibling", "Zack was supposed to be at the dorm before 3:30 PM", "Derrick's watch stopped at 3:34 PM", "Someone was looking for something at the crime scene", "Derrick thinks he saw Ben at the crime scene"], twistID)
	print '}'
conlb(twistID)
twist1=judgePopup(Toplevel(root), (0, 5), (abcd, cproof), #answer: No, proof: Charlie was on a flight at the time of the murder. twist1.result produces True if the player was correct and False if incorrect.
"You: 'Yes, we can let you go. Remove his handcuffs, he can't have committed the crime if he was confirmed by the airlines to have been on a flight at the time the vitim was killed.' Richard looks at you approvingly, but doesn't seem surprised.",
"You spout out the wrong answer, and Richard bows his head in disappointment. He corrects you.\nRichard: 'No, we obviously CAN let him go. Look at your info. Charlie was on a flight back to Wyoming from 2:00 PM to 6:00 PM, putting him thousands of metres in the air at the time of the murder, which was some time around 4:00 PM.")
script=["Richard then stands up and removes the cuffs from Charlie before leading him out of the station.",
"After some time, Richard returns with another handcuffed suspect.", "Richard: 'This is Derrick. Take a seat, Derrick.'", "Derrick complies silently and easily, sitting down across from you.",
"You expected more resistance.", "Richard: 'Start out by telling us everything you know.'", "Derrick: 'Alright. I'm Zack's roommate. Well, was, anyways.'",
"Derrick: 'He was supposed to be back in the dorm before, at the most, 3:30 PM.'", "Derrick: 'He didn't show up, but I left the door unlocked for him anyways, figuring he was just a late or something because he was preparing for the party -- or whatever it was.'"
"Derrick: 'I was watching TV, waiting for him to come home when, suddenly, I heard the front door open.", "Derrick: I'm not sure who it was, but at the time I assumed it was Zack. I stood up and went to go talk to him, but when I exited the doorway, I was knocked to the floor. Just before I hit the ground, I think I saw Ben.",
"I don't remember anything after that until I woke up in custody.'", "Richard: 'Interesting. You only THOUGHT you saw him briefly before you hit the ground. Oh. Right. We found a broken watch on his wrist, stopped at 3:34 PM. Forgot to tell you.'",
"You sigh. How many other pieces of evidence has this idiot forgotten to tell you about?", "Richard: 'Oh -- and the crime scene was a mess. Not just in a way typical of a struggle. It's almost as if someone was frantically searching for something.'",
"You give Richard a look of disappointment and turn back to Derrick, asking him a few questions.", "You: 'You mentioned before that you knew Richard was having a party. Do you know what for?'",
"Derrick: 'I think Zack said something about getting tons of inheritance money from his grandmother, but I don't remember. He was pretty heartless, that Zack.'", "Something clicks. Richard sees your eyes light up.",
"Richard: 'What's up? Figure something out?'", "Fill this popup by choosing option A, B, C, or D and then picking a proof from the list of things you already know.",
"You: 'The motive was ' \n\nA. 'revenge.'\n\nB. Derrick's desire to move out.'\n\nC. 'greed.'\n\nD. 'to convict Derrick of a crime he didn't commit.'", '!A']
abcd=0; cproof=0
root.update()
while twistID==1:
	print 'mainloop2 {'
	root.mainloop()
	print '	',abcd,':',cproof #the '	' is just for formatting purposes.
	if checkpoint.get():
		checkpoint.set(False)
		four=objReturner.get()
	cproof=four.vsel
	abcd=four.opt.get()
	twistID=checkIfDone(four, prooflist, ["The motive was greed", "Zack inherited tons of money from his grandmother", "Inheritance passed by birth order", "Only Zack knew the full contents of the will", "The money was supposed to arrive in 2 years' time"], twistID)
	print '}'
conlb(twistID)
twist2=judgePopup(Toplevel(root), (2,12), (abcd, cproof), "You: 'The motive was greed; the culprit wanted the inheritance money, and he or she tore the place up looking for it. Additionally, the culprit has to have been a family member or close friend to have known about the money. Richard, can you obtain a copy of her will?",
"Richard ponders your conclusion for a moment, and then denies it.\nRichard: 'That doesn't seem right. The only thing I can see is that the motive was greed. The dorm was scattered as if someone were looking for something, something they would kill for. People would kill for large sums of money, and . Therefore, Zack was probably killed for his grandmother's inheritance money. I'll go see if I can get a copy of her will. Stay here.'")
script=["...And with that, Richard left the room. About an hour later, he returns with a document, catching you about to fall asleep.",  "Richard: 'Sorry for the wait. It was a little harder to get ahold of this than I thought it would be.'",
"Glad that he did show up, you take the document. On it, you find something rather interesting. All 1 billion dollars of her inheritance was to go to her daughter's oldest son. Only he is to be told the contents of this will.",
"Should he be unable to recieve the money in 2 years' time, the money should go to her daughter's next oldest son.",
"You: 'Good news, Derrick. I've ruled you out as a possible suspect.'", "Richard: 'How?'", "You: 'Didn't you read the document?'", "Richard: 'Of course.'",
"Your faith in the police force is declining at a rapid rate.", "You: 'Well, it specifies that the inheritance should only be passed on to her relatives, as most do. Therefore, since Derrick is not a relative of Zack, he can't have killed Zack for the money.'",
"Richard: 'Oh. Well. Uh, who should I bring in next?'", "You: 'Bring in Ben, please.'", "Richard nods, and walks Derrick out of the station. Finally, two viable suspects.", "Shortly after he leaves, Richard returns.",
"Ben looks upset and somewhat angry as he sits down across from you. Something seems off, but you ignore it.", "You: 'I'd like to get straight to the point here, Ben. I'll just ask you questions, and ask that you answer them all honestly.'",
"Ben: 'Mhm.'", "You: 'Thank you for you cooperation.'", "Ben: 'Yeah, whatever.'", "His apathy disturbs you, but you press on.", "You: 'Did you know that Zack was supposed to be having a family gathering on the 14th of December?'",
"Ben: 'Yeah, I was on my way there. When I got there, there were police everywhere. I tried to get in but when I told one of them my name, he arrested me. Someone is trying to frame me and I know it!!'", "You: 'Calm down, Ben.'",
"If someone were trying to frame Ben, the only person I could think of is Derrick, but he isn't the culprit and has no reason to try to frame Ben. Odd.", "You: 'So you're saying you didn't kill Zack the--'", "Ben: No! I'll bet my twin, Aaron, did it.", "...Do I believe Ben?", '!B']
abcd=0; cproof=0
root.update()
while twistID==2:
	print 'mainloop3 {'
	root.mainloop()
	print '	',abcd,':',cproof
	if checkpoint.get():
		checkpoint.set(False)
		two=objReturner.get()
	cproof=two.vsel
	abcd=two.opt.get()
	twistID=checkIfDone(two, prooflist, [""], twistID)
	print '}'
twist3=judgePopup(Toplevel(root), (1,16), (abcd, cproof), "You: 'Don't worry, I believe you.'", "You remain silent, and continue interviewing Ben. Afterwards, you interview Aaron, but can't find him guilty either.'", (1,9)) #1, 9 could also be correct. By saying that you believe him because he is the youngest, you are implying that you know why that is significant.
print twist1.result, twist2.result, twist3.result
if twist1.result == False and twist2.result == False and twist3.result == False:
	print "BADEND"
	script=["The case grows cold, and soon after you hear urban legends of a deadly desire for a billion dollars, and a culprit by the name of Aaron walking free.", "With nothing to go on but a legend, you live your life knowing you are responsible for the failure, and Zack's family never get to know who it was who killed their beloved son: their second most beloved son."]
if twist1.result or twist2.result or twist3.result:
	print "STDEND"
	script=["Suddenly, Richard has an epiphany.", "Richard: 'It WAS Aaron! If the motive was greed, then if Ben was the killer, he would have had to kill Aaron as well to get the money because Ben is the youngest! Aaron, however, only had to kill Zack if he wanted the money! It's THAT simple!! Furthermore, Derrick thought he saw Ben at the crime scene, but since Aaron and Ben are twins, as Ben mentioned, it could have been either one he saw.'", "You are mentioned at the bottom of the newspaper article as being a 'renowned private investigator' who aided the police.",
	"Somehow, you feel you deserve a bit more credit than that, but you still got a spike in business, so you can't complain."]
if twist1.result and twist2.result and twist3.result:
	print "GOODEND"
	script=["You explain to Richard what you have deduced, and he seems amazed for some reason.", "You: 'The motive was greed, however, Ben was the youngest, and the will specifies the inheritance will be passed down by birth order if the current candidate is unable to recieve the money, therefore if Ben was the killer, he would have also killed Aaron, the next candidate for the inheritance. Since Aaron is alive, and did not report being attacked, we can deduce that he was the killer.","In addition, if Aaron and Ben are twins, then the person Derrick thought he saw when he was attacked could have been either. Since Ben has no reason to want the money, he would have no reason to attack potential witnesses. Therefore, Aaron is also responsible for the attack on Derrick.'", "After the investigation concludes, you are proven correct. You become the most famous private investigator in the world, heralded as 'The modern Sherlock Holmes'. Your firm becomes worth more than 1 billion dollars."]
script.append("- FIN - ")
while twistID==3:
	print 'mainloop final {'
	root.mainloop()
	print '}'
print "- FIN -"
