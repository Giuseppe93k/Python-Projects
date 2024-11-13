import tkinter as tk


from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #sets title of GUI window
        self.master.title("File Transfer")

        #Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Positions  source button in the GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30,0))

        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #Creates button to select destination of files from directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Position destination button in GUI using tkinter grid()
        #on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15, 10))

        #creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Position transfer siles button
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0, 15))

        #creates an Exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #position the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    #Creates a function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the the content that is inserted in the Entry widget,
        #this allows the path to be inserted iunto the Entru widget properly.
        self.source_dir.delete(0, END)
        #the .insert method will insert the user selection to the source_dirEntry
        self.source_dir.insert(0, selectSourceDir)


    #creates function to select destination directoty
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content that is inserted in the Entry eidget,
        #this allows the path to be inserted into the Entry widget properly.
        self.destination_dir.delete(0, END)
        #the  .insert methos will insert the user selection to the destination_dir Entry widget
        self.destination_dir.insert(0, selectDestDir)


    #creates function to transfer files from one directory to another
    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #gets list of files in the source directory
        source_files = os.listdir(source)
        #time now and 24 hours ago
        now = datetime.now()
        before_24_hours = now - timedelta(hours=24)
        #running through each file in the source directory 
        for i in source_files:
            #full path of the file 
            full_path = os.path.join(source, i)
            #getting the last modified time of the file 
            file_mtime = datetime.fromtimestamp(os.path.getmtime(full_path))
            #checks if the file was modified in the last 24 hours
            if file_mtime > before_24_hours:
                #moves each file from the source directory to the destination directory
                shutil.move(full_path, destination)
                print(f"{i} was succefully transferred.")

    #creates function to exit program
    def exit_program(self):
        #root is the main GUI window, the Tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()
    


        
    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
