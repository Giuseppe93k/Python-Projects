
from tkinter import *
import tkinter as tk

#importing my other modules 
import StudentsTracking_main
import StudentsTracking_func


def load_gui(self):
    self.lbl_fname = tk.Label(self.master,text='First Name:')#defining it 
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)#placing it 
    self.lbl_lname = tk.Label(self.master,text='Last Name:')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_phone = tk.Label(self.master,text='Phone Number:')
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_email  = tk.Label(self.master,text='Email Address:')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_course = tk.Label(self.master,text='Course:')
    self.lbl_course.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_student = tk.Label(self.master,text='Students:')
    self.lbl_student.grid(row=0,column=2,padx=(0,0),pady=(10,0),sticky=N+W)

    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_course = tk.Entry(self.master,text='')
    self.txt_course.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    #define the lightbox with scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>',lambda event: StudentsTracking_func.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S)
    
    #defining and placing my to buttons 
    self.btn_Submit = tk.Button(self.master,width=12,height=2,text='Submit',command=lambda: StudentsTracking_func.addToList(self))
    self.btn_Submit.grid(row=10,column=2,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: StudentsTracking_func.onDelete(self))
    self.btn_delete.grid(row=10,column=6,padx=(15,0),pady=(45,10),sticky=W)
    

    StudentsTracking_func.create_db(self)
    



if __name__ == "__main__":
    pass
