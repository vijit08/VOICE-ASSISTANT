from tkinter import *

root=Tk()
root.geometry("634x434")
def hello():
    print("hello vijit")


f=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f.pack(side="left",anchor="nw")
b1=Button(f,bg="yellow",text="print",command=hello)
b1.pack()

root.mainloop()
