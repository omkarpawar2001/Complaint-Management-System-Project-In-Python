#!/usr/bin/python3
import os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.ttk import Style

from db import DBConnect
from listComp import ListComp
from listTech import ListTech
from bar import ListBar
from bar2 import ListBar2
from bar3 import ListBar3
from PIL import Image, ImageTk
from tkinter import Button

# Config
conn = DBConnect()
root = Tk()
root.geometry('800x400')
root.title('Register Complaint | Complaint Management')
root.configure(background='#FFFFCC')

# Style
style = Style()
image1 = Image.open("img1.jpg")
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)



# Gridx1353
labels = ['Full Name:', 'Type of User:', 'Type of Complaint:', 'Describe Your Issue:']
for i in range(4):
    Label(root, text=labels[i]).grid(row=i+1, column=0, padx=10, pady=10)

BuSubmit = Button(root, text='Submit Now', font=('Arial', 11))
BuSubmit.grid(row=5, column=3, padx=20, pady=20)

# Entries
fullname = Entry(root, width=40, font=('Arial', 14))
fullname.grid(row=1, column=1, columnspan=2)
SpanGender = StringVar()
Radiobutton(root, text='Faculty', value='Faculty', variable=SpanGender).grid(row=2, column=1)
Radiobutton(root, text='Student', value='Student', variable=SpanGender).grid(row=2, column=2)
SpanType = StringVar()
Radiobutton(root, text='Hardware', value='Hardware', variable=SpanType).grid(row=3, column=1)
Radiobutton(root, text='Software', value='Software', variable=SpanType).grid(row=3, column=2)
Radiobutton(root, text='Other', value='Other', variable=SpanType).grid(row=3, column=3)
comment = Text(root, width=40, height=5, font=('Arial', 14))
comment.grid(row=4, column=1, columnspan=2, padx=10, pady=10)


def SaveData():
    msg = conn.AddComplaints(fullname.get(), SpanGender.get(), SpanType.get(), comment.get(1.0, 'end'))
    fullname.delete(0, 'end')
    comment.delete(1.0, 'end')
    showinfo(title='Add Info', message=msg)


def ShowList():
    listrequest = ListComp()


def ShowTech():
    os.system('python technician.py')




def ShowStatus():
    os.system('python main.py')


BuSubmit.config(command=SaveData)

root.mainloop()
