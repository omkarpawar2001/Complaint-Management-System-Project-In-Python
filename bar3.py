from tkinter import *
from tkinter.ttk import *
from db import DBConnect
import sqlite3
import numpy as np
import matplotlib.pyplot as plt


class ListBar3:
    def __init__(self):
        conn = sqlite3.connect('information.db')
        c = conn.cursor()
        self._dbconnect = DBConnect()
        self._dbconnect.row_factory = sqlite3.Row
        c.execute('select Status,COUNT(*) AS Status from Status GROUP BY Status')
        data = c.fetchall()
        dates = []
        values = []
        for row in data:
            dates.append(row[0])
            values.append(row[1])
        f = plt.figure()
        f.set_figwidth(11)
        f.set_figheight(4)
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
        plt.bar(dates, values,color=colors)
        plt.title("Graph Showing Analysis of Complaint Status")
        plt.xlabel('Status of the Complaints')
        plt.ylabel('Number of Complaints Recieved')
        plt.show()




