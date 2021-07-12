#!/usr/bin/python3
import os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.ttk import Style
from listComp import ListComp
from listTech import ListTech
from bar import ListBar
from bar2 import ListBar2
from bar3 import ListBar3
from PIL import Image, ImageTk
import tkinter.font as font
from tkinter import Button

root = Tk()
root.geometry('800x400')
root.title('Home | Complaint Management')

# Style
style = Style()
image1 = Image.open("imgresize.jpg")


photo = PhotoImage(file="2.png")

#btnbg = Image.open("bg.png")
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)

#my_label = Label(root, text=" Complaint Management System ", font=('Colonna MT', 30,'bold'),fg='white',bg='lightcoral')
#my_label.place(x=130, y=50)


regcom = Button(root, text='Register Complaint',width='20',bg='black',fg='white',font=('Arial', 13,'bold'))
regcom.place(x=550, y=130)

listcom = Button(root, text='List Complaints',width='20',bg='black',fg='white', font=('Arial', 13,'bold'))
listcom.place(x=550, y=180)

stscom = Button(root, text='Check / Change \nStatus of a Complaint',width=20,bg='black',fg='white', font=('Arial', 13,'bold'))
stscom.place(x=550, y=230)

addtech = Button(root, text='Add a Technician',width='20',bg='black',fg='white', font=('Arial', 13,'bold'))
addtech.place(x=550, y=300)

analysis = Button(root, text='Do Analysis',width='20',bg='black',fg='white', font=('Arial', 13,'bold'))
analysis.place(x=550, y=350)

def register():
    os.system('python home.py')
def ShowList():
    listrequest = ListComp()
def ShowStatus():
    os.system('python status.py')
def ShowTech():
    os.system('python technician.py')
def ShowAnalysis():
    os.system('python analysis.py')


regcom.config(command=register)
listcom.config(command=ShowList)
stscom.config(command=ShowStatus)
addtech.config(command=ShowTech)
analysis.config(command=ShowAnalysis)
root.mainloop()
