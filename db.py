#!/usr/bin/python3
import sqlite3



class DBConnect:
    def __init__(self):
        self._db = sqlite3.connect('information.db')
        self._db.row_factory = sqlite3.Row
        self._db.execute('create table if not exists Complaints(ID integer primary key autoincrement, '
                         'Name varchar(255), User varchar(255), Type varchar(255),Description text)')
        self._db.execute('create table if not exists Technician(ID integer primary key autoincrement, '
                         'Name varchar(255), Gender varchar(255), Specification varchar(255))')
        self._db.execute('create table if not exists Status(ID integer, Status varchar(255))')
        self._db.commit()

    def AddComplaints (self, name, user, type1, comment):
        self._db.execute('insert into Complaints(Name, User, Type, Description) values (?,?,?,?)',
                         (name, user, type1, comment))
        self._db.commit()
        return 'Your complaint has been submitted!!!'

    def AddStatus(self, id1, status):
        self._db.execute('insert into Status(ID,Status) values (?,?)', (id1, status))
        self._db.commit()
        return 'Status has been updated!!!.'

    def AddTechnician(self, name, spec):
        self._db.execute('insert into Technician(Name, Specification) values(?,?)', (name, spec))
        self._db.commit()
        return 'Technician Registered Succesfully!!!'

    def ListRequest(self):
        cursor = self._db.execute('select * from Complaints')
        return cursor

    def ListReq(self):
        cursor = self._db.execute('select * from Technician')
        return cursor

    def ListStatus(self):
        cursor = self._db.execute('select * from Status')
        return cursor
