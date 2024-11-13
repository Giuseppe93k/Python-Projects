
import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        
        #creating the button foe the default html page 
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0 , padx=(10, 10), pady=(10, 10))
        
        #creating the button foe the default html page
        self.btn2 = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn2.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))
        
        
        #creating a label and entry box to insert custom text
        self.label = Label(self.master, text="Enter custom text or click the Default HTML button")
        self.label.grid(row=0, column=0, columnspan=2,padx=(10, 10), pady=(10, 10))
        
        self.btn_custom = Entry(self.master,width=100)
        self.btn_custom.grid(row=1, column=0, columnspan=2,padx=(10, 10), pady=(10, 10))
        


    #default text for the default webpage if you dont input text
    def defaultHTML(self):
        htmlText = "Stay tuned for out amazing summer sale!"
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        with open("index.html", "w") as htmlFile:
            htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    #gives you a webpage with a custom text inputed by user 
    def customHTML(self):
        htmlText = self.btn_custom.get()
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        with open("index.html", "w") as htmlFile:
            htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

        




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
