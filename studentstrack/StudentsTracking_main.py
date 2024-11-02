#Python Ver:   3.12.3
#
#Author:       Giuseppe Kakra
#
#Purpose:      Student Tracking App, Demostrating OOP, Tkinter GUI Module,
#              using Tkinter Parent and Child relationships.
#
#Tested OS:    This code is written and tested to work with Windows 10 and above.

from tkinter import *
import tkinter as tk
import sqlite3

#Importing all my modules
import StudentsTracking_gui
import StudentsTracking_func


#tkinter frame class that our my class will inherit 
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #defining the master frame configuration
        self.master  = master
        self.master.minsize(800,600)#(Height,Width)
        self.master.maxsize(800,600)
        #CenterWindow method will center my app on the user's screen
        StudentsTracking_func.center_window(self,800,600)
        self.master.title("Students Course Tracking")
        self.master.configure(bg="#F0F0F0")
        #This protocol method is a tkinter vuilt-in method to catch if
        #the user clicks the upper corner, "X" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: StudentsTracking_func.ask_quit(self))
        arg = self.master

        #loading the GUi widgets from a separate module
        StudentsTracking_gui.load_gui(self)
        
#loading the list in the Listbox
    def update_listbox(self):
        self.lstList1.delete(0, END)  # Clear the Listbox
        conn = sqlite3.connect('db_TrackS.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT col_fullname FROM tbl_Students")
            data = cursor.fetchall()
            for item in data:
                self.lstList1.insert(END, item[0])  # Insert each item into the Listbox
        conn.close()



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
