from tkinter import *
from tkinter.ttk import *
from db import DBConnect
import sqlite3

class ListComp:
	def __init__(self):
		self._dbconnect = DBConnect()
		self._dbconnect.row_factory = sqlite3.Row
		self._root = Tk()
		self._root.title('List of Complaints | Complaint Management')
		tv = Treeview(self._root)
		tv.pack()
		tv.heading('#0', text='ID')
		tv.configure(column=('#Name', '#User', '#Type', '#Description'))
		tv.heading('#Name', text='Name')
		tv.heading('#User', text='User')
		tv.heading('#Type', text='Type')
		tv.heading('#Description', text='Description')
		cursor = self._dbconnect.ListRequest()
		for row in cursor:
			tv.insert('', 'end', '#{}'.format(row['ID']),text=row['ID'])
			tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
			tv.set('#{}'.format(row['ID']),'#User',row['User'])
			tv.set('#{}'.format(row['ID']),'#Type',row['Type'])
			tv.set('#{}'.format(row['ID']), '#Description', row['Description'])
			
