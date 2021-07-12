from tkinter import *
from tkinter.ttk import *
from db import DBConnect
import sqlite3


class ListStatus:
    def __init__(self):
        self._dbconnect = DBConnect()
        self._dbconnect.row_factory = sqlite3.Row
        self._root = Tk() 
        self._root.title('List of Status | Complaint Management')
        conn = sqlite3.connect('information.db')
        cursor = conn.cursor()
        tree = Treeview(self._root, columns=("ID", "Status"))
        #tree.heading('ID', text="ID", anchor=W)
        tree.heading('Status', text="Status", anchor=W)
        tree.pack()
        tree.delete(*tree.get_children())
        DBConnect()
        cursor.execute("SELECT * FROM Status")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1]))
        cursor.close()
        conn.close()


