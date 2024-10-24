import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
from PIL import Image, ImageTk

class Help:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System") 
        
        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        imgtop=Image.open(r"college_images\helpdesk.jpeg")
        imgtop=imgtop.resize((1530,720),Image.LANCZOS)
        self.photoimgtop=ImageTk.PhotoImage(imgtop)
        bg_img=Label(self.root,image=self.photoimgtop)
        bg_img.place(x=0,y=55,width=1530,height=720)
        
        dev_label=Label(bg_img,text="Email:aryanmishra@gmail.com",font=("time new roman",20,"bold"),bg="white")
        dev_label.place(x=550,y=260)

if __name__== "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
  