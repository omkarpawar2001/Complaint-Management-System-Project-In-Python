from tkinter import *
from tkinter.ttk import *
from db import DBConnect
import sqlite3

class ListTech:
	def __init__(self):
		self._dbconnect = DBConnect()
		self._dbconnect.row_factory = sqlite3.Row
		self._root = Tk()
		self._root.title('List of Technicians | Complaint Management')
		tv = Treeview(self._root)
		tv.pack()
		tv.heading('#0', text='ID')
		tv.configure(column=('#Name', '#Specification'))
		tv.heading('#Name', text='Name')
		tv.heading('#Specification', text='Specialization')
		cursor = self._dbconnect.ListReq()
		for row in cursor:
			tv.insert('', 'end', '#{}'.format(row['ID']),text=row['ID'])
			tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
			tv.set('#{}'.format(row['ID']))
			tv.set('#{}'.format(row['ID']),'#Specification',row['Specification'])
			
