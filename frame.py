from tkinter import *

root=Tk()
root.geometry("634x434")
f1=Frame(root,bg="grey",borderwidth=6,relief=GROOVE)
f1.pack(side="left",fill="y")

f2=Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(side="top",fill="x")

l=Label(f1,text="nigga has died")       #SIDE BAR
l.pack(pady=142)

l=Label(f2,text="PYCHARM PROJJECT",font="algerian 12",padx=20)
l.pack()
root.mainloop()
