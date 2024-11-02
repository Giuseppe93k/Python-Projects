#Python Ver:   3.12.3
#
#Author:       Giuseppe Kakra
#
#Purpose:      Student Tracking App, Demostrating OOP, Tkinter GUI Module,
#              using Tkinter Parent and Child relationships.
#
#Tested OS:    This code is written and tested to work with Windows 10 and above.


import os
from tkinter import *
import tkinter as tk
import sqlite3

#importing my other modules 
import StudentsTracking_main
import StudentsTracking_gui
from tkinter import messagebox



def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get screen and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    #calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


#catch if user's clicks on the upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #this is close app
        self.master.destroy()
        os._exit(0)#cleaning up the memmory when the app closes


def create_db(self):
    conn = sqlite3.connect('db_TrackS.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_Students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        # commiting the changes in other to create the database and close it 
        conn.commit()
    conn.close()
    first_run(self)
    self.update_listbox()

def first_run(self):
    conn = sqlite3.connect('db_TrackS.db')
    with conn:
        cur  = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_Students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", ('John','Doe','John Doe','135-111-8465','jdoe@email.com','IT'))
            cur.execute("""INSERT INTO tbl_Students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", ('Giuseppe','Kakra','Giuseppe Kakra','546-984-8498','gkakra@email.com','cyber security'))
            cur.execute("""INSERT INTO tbl_Students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", ('Naomi','Kendal','Naomi Kendal','516-198-9842','Nkendal@email.com','beaty makeup'))
            conn.commit()
    conn.close()
    self.update_listbox()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_Students""")
    count = cur.fetchone()[0]
    return cur,count

#select item Listbox
def onSelect(self,event):
    #calling the event is the self.lstList1 widget
    varList = event.widget
    if varList.curselection():
        select = varList.curselection()
        value = varList.get(select)
        conn = sqlite3.connect('db_TrackS.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_Students WHERE col_fullname = (?)""",[value])
            varBody = cursor.fetchall()
            #This returns a tuple and we can slice it into 4 parts using data[] during the iteration
            for data in varBody:
                self.txt_fname.delete(0,END)
                self.txt_fname.insert(0,data[0])
                self.txt_lname.delete(0,END)
                self.txt_lname.insert(0,data[1])
                self.txt_phone.delete(0,END)
                self.txt_phone.insert(0,data[2])
                self.txt_email.delete(0,END)
                self.txt_email.insert(0,data[3])
                self.txt_course.delete(0,END)
                self.txt_course.insert(0,data[4])
    
#this is my addToList method to linked with the submit button
def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    var_fullname = f"{var_fname} {var_lname}"
    var_phone = self.txt_phone.get()
    var_email = self.txt_email.get()
    var_course = self.txt_course.get()

    conn = sqlite3.connect('db_TrackS.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tbl_Students (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?, ?, ?, ?, ?, ?)", 
                       (var_fname, var_lname, var_fullname, var_phone, var_email,var_course))
        self.lstList1.insert(END, var_fullname)
        
    conn.commit()
    conn.close()

#this function deletes a student from the list when you click Delete
def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())  # Listbox's selected value
    conn = sqlite3.connect('db_TrackS.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM tbl_Students")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete confirmation", f"All information associated with ({var_select}) \nwill be permanently deleted from the database.\n\nProceed with the request?")
            if confirm:
                cur.execute("DELETE FROM tbl_Students WHERE col_fullname = ?", (var_select,))
                onDeleted(self)
                conn.commit()
        else:
            messagebox.showerror("Last Record Error", f"({var_select}) is the last record in the database and cannot be deleted at this time.\n\nPlease add another record first before you can delete ({var_select}).")
    conn.close()   


def onDeleted(self):
    #clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass



if __name__ == "__main__":
    pass
