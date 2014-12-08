from Tkinter import *
from fourbttngui import *
from listpopup import *
from tspopup import *

def createFourBttn(proofs):
	fbttn=fourBttn(Toplevel(root), proofs)
	pass
def createListPopup(inlist):
	lpopup=listPopup(Toplevel(root), inlist)
def createTranscriptPopup(transcript): #if I'm gonna do a transcript thing, I should have a print function which adds stuff to the transcript log too.
	tpopup=transcriptPopup(Toplevel(root), transcript)
	pass

transcript1=("You are a terrible person."*25)                                                                               #type a
transcript2=(('Player', "Blah blah blah blah blah blah"), ('Suspect', "BLAH! Blah blah blah BLAH."), ('Player', "Blah...")) #type b
TESTLIST=["Knife is victim's", "Killer entered prior to 4 PM", "Suspect's name is written in blood"]
root=Tk() #creating a child class or just a class using this creates more problems than it solves. I learned that from experience.
storymsg=Message(root, text='THIS IS A TEST MESSAGE')
storymsg.pack(side=BOTTOM, anchor=CENTER, fill=X, expand=1)
storymsg.bind("<Configure>", lambda e: storymsg.configure(width=e.width-10)) #I had to use a lambda here because the function I'm calling needs an argument.
Button(root, text="Proofs", command=lambda: createListPopup(TESTLIST)).pack(side=TOP, anchor=NW, expand=1)  #Also, should have an image in this button instead of words.
Button(root, text="Transcript", command=lambda: createTranscriptPopup(transcript2)).pack(side=TOP, anchor=NW, expand=1)
Button(root, text="DEBUG: CREATE fourBttn", command=lambda: createFourBttn(TESTLIST)).pack(side=BOTTOM)
four=fourBttn(Toplevel(root), TESTLIST)
selection = 0
while True:
	root.mainloop()
	#[if statement that triggers when a popup window has been launched]
	print four.root.pack_slaves()
	selection=four.vsel
	print selection