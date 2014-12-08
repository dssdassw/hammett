from Tkinter import *
from fourbttngui import *
from listpopup import *
import random

def createFourBttn():
	pass
def createListPopup():
	pass

TESTLIST=["Knife is victim's", "Killer entered prior to 4 PM", "Suspect's name is written in blood"]
root=Tk() #creating a child class or just a class using this creates more problems than it solves. I learned that from experience.
Message(root, text='THIS IS A TEST MESSAGE').pack()
Button(root, text="Proofs").pack()
app = fourBttn(Toplevel(root), TESTLIST)
b=listPopup((Toplevel(root)).geometry('300x400-5+40'), TESTLIST)
selection=0
while True:
	root.mainloop()
	#[if statement that triggers when a popup window has been launched]
	selection=app.vsel