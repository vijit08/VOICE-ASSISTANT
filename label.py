from tkinter import *

root=Tk()

root.title("VIJITS GUI")
root.geometry("534x334")
root=Label(text="Tkinter is a Python binding to the Tk GUI toolkit. \nIt is the standard Python interface to the Tk GUI toolkit, \nand is Python's de facto standard GUI.\n Tkinter is included with standard Linux, Microsoft Windows and Mac OS X installs of Python.\n The name Tkinter comes from Tk interface", bg="red",padx=25,pady=30,font=("algerian",10),borderwidth=4,relief=SUNKEN)

root.pack(side ="left",anchor="nw",fill=Y,padx=34,pady=40)

root.mainloop()
