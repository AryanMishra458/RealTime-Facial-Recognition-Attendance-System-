import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System") 
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        imgtop=Image.open(r"college_images\dev.jpg")
        imgtop=imgtop.resize((1530,720),Image.LANCZOS)
        self.photoimgtop=ImageTk.PhotoImage(imgtop)
        bg_img=Label(self.root,image=self.photoimgtop)
        bg_img.place(x=0,y=55,width=1530,height=720)
        
        #Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)
        
        imgtop1=Image.open(r"college_images\aryan.jpg")
        imgtop1=imgtop1.resize((200,200),Image.LANCZOS)
        self.photoimgtop1=ImageTk.PhotoImage(imgtop1)
        bg_img=Label(main_frame,image=self.photoimgtop1)
        bg_img.place(x=300,y=10,width=200,height=300)
        
        imgtop2=Image.open(r"college_images\niharika.jpg")
        imgtop2=imgtop2.resize((200,200),Image.LANCZOS)
        self.photoimgtop2=ImageTk.PhotoImage(imgtop2)
        bg_img=Label(main_frame,image=self.photoimgtop2)
        bg_img.place(x=300,y=320,width=200,height=200)
        
        
        #Developer info
        dev_label=Label(main_frame,text="Aryan Mishra and Niharika Valacha",font=("time new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)
        
        img2 = Image.open(r"college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2 = img2.resize((550, 300), Image.LANCZOS)  
        self.photoimg2 = ImageTk.PhotoImage(img2)
    
        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=210, width=300, height=300)
       
        
       
if __name__== "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
  