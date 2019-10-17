
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from tkinter.ttk import Combobox
import sys
import optparse
import re
import shutil
import os

def browse():
    path = root.folderpath = filedialog.askdirectory()
    pathvalue.set(path)
    if(len(path) is not 0):
        os.chdir(path)
    
    print(os.getcwd())
    
def getvals():
    if(filevalue.get()=="All"):
        document()
        compress()
        video()
        program()
        picture()
        
    if(filevalue.get()=="Document"):
        document()
    if(filevalue.get()=="Compressed"):
        compress()
    if(filevalue.get()=="Video"):
        video()
    if(filevalue.get()=="program"):
        program()
    if(filevalue.get()=="Picture"):
        picture()


def document():
    string = os.listdir(".")
    tf = os.path.isdir("Documents")
    if tf is False:
        try:
            os.mkdir("Documents")
        except:
             tkinter.messagebox.showinfo("File Assembling Manager", "Oops! Can't Make Directory")
             
    
    r1 = []
    comp = ""
    for i in string:
        r = re.findall(r'^.*\.(txt|xls|c|out|doc|pptx?|pdf)', i)
        if len(r) > 0:
            shutil.move(i, 'Documents')
        else:
            pass
    print("Successfully moved Docs")
    tkinter.messagebox.showinfo("File Assembling Manager", "Documents Assembled Successfully!")
            



def compress():
    string = os.listdir(".")
    tf = os.path.isdir("Compressed")
    if tf is False:
          try:
            os.mkdir("Compressed")
          except:              
              tkinter.messagebox.showinfo("File Assembling Manager", "Oops! Can't Make Directory")
    r1 = []
    comp = ""
    for i in string:
        r = re.findall(r'^.*\.(zip|tar.xz|tar.gz|rar)', i)
        if len(r) > 0:
            shutil.move(i, 'Compressed')
        else:
            pass
    print("Successfully moved Compressed files")
    tkinter.messagebox.showinfo("File Assembling Manager", "Compressed Assembled Successfully!")
     

def video():

    string = os.listdir(".")
    tf = os.path.isdir("Videos")
    if tf is False:
        try:
            os.mkdir("Videos")
        except:
             tkinter.messagebox.showinfo("File Assembling Manager", "Oops! Can't Make Directory")

    r1 = []
    comp = ""
    for i in string:
            
        r = re.findall(r'^.*\.(mp4|mkv)', i)
        if len(r) > 0:
            shutil.move(i, 'Video')
        else:
            pass
    print("Successfully moved Videos")
    tkinter.messagebox.showinfo("File Assembling Manager", "Videos Assembled Successfully!")
     
    

def program():

    string = os.listdir(".")
    tf = os.path.isdir("programs")
    if tf is False:
        try:
            os.mkdir("Programs")
        except:
             tkinter.messagebox.showinfo("File Assembling Manager", "Oops! Can't Make Directory")
    r1 = []
    comp = ""
    for i in string:
            
        r = re.findall(r'^.*\.(py|html|exe|jar|bin)', i)
        if len(r) > 0:
            shutil.move(i, 'programs')
        else:
            pass
    print("Successfully moved programs")
    tkinter.messagebox.showinfo("File Assembling Manager", "Programs Assembled Successfully!")
     

def picture():
    string = os.listdir(".")
    tf = os.path.isdir("Pictures")
    if tf is False:
        try:
            os.mkdir("Pictures")
        except:
             tkinter.messagebox.showinfo("File Assembling Manager", "Oops! Can't Make Directory")
         
    r1 = []
    comp = ""
    for i in string:
        r = re.findall(r'^.*\.(jpg|png|jpeg|JPEG|PNG|mp3)', i)
        if len(r) > 0:
            shutil.move(i, 'Pictures')
        else:
            pass
    print("Successfully moved Pictures")
    tkinter.messagebox.showinfo("File Assembling Manager", "Pictures Assembled Successfully!")
     
#**********GUI code***************

root = Tk()
root.geometry("320x100")
root.maxsize(300,100)
root.minsize(300,100)
root.title("File Assembling Manager")
root.wm_iconbitmap("icon.ico")
label_on_screen = Label(root, text="File Assembling Manager")

#********path Section Start
folder_path = Label(root, text="Folder Path")
label_on_screen.grid(column=1)
folder_path.grid(row=1)
pathvalue = StringVar()
pathentry = Entry(root, textvariable = pathvalue)
pathentry.grid(row=1, column=1)
Button(text="Browse",width = 10, command=browse).grid(row=1, column=2)
#**************path section end

#******combobox section start****
filevalue = StringVar()
file_type = Label(root, text="File Type")
v = ["All", "Document", "Compressed","Video","program","Picture"]
combo = Combobox(root, textvariable=filevalue, values = v, height=4, width = 17)
combo.set("select")
file_type.grid(row=2, column=0)
combo.grid(row=2, column=1)
Button(root,text="Assemble", width=10, command=getvals).grid(row=2, column=2)
#combobox section end*****

Button(root,text="Exit", width=10, command=root.destroy).grid(row=3, column=2)
root.mainloop()
