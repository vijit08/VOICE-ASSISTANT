from tkinter import *
from PIL import Image,ImageTk

vijit_root=Tk()

vijit_root.geometry("534x334")

photo=Image.open("three.jpg")
img=ImageTk.PhotoImage(photo)

vijit=Label(image=img)
vijit.pack()

#FOR JPEG Image




vijit_root.mainloop()























"""
photo1=Image.open("three.jpg")
image1=ImageTk.PhotoImage(photo1)

label=Label(image=image1)
label.pack()
"""
