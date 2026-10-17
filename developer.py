from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")

        title_lbl = Label(
            self.root,
            text="DEVELOPER",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="blue",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"E:\face recognisation model\potos\developers.jpg")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl3 = Label(self.root, image=self.photoimg_top)
        f_lbl3.place(x=0, y=55, width=1530, height=720)

        #frame
        main_frame = Frame(f_lbl3, bd=2, bg="grey")
        main_frame.place(x=0, y=0, width=400, height=400)
        
        img_top1 = Image.open(r"E:\face recognisation model\potos\developer1.jpg")
        img_top1 = img_top1.resize((200, 230), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl3 = Label(main_frame, image=self.photoimg_top1)
        f_lbl3.place(x=100, y=0, width=200, height=230)

#developer details
        developer_label = Label(main_frame, text="Hello, I am Rahul ", font=("ALGERIAN", 25, "bold"),fg="orange",  bg="grey")
        developer_label.place(x=40, y=230)

        developer_label = Label(main_frame, text="I am the developer of this Facial \n Recognition model", font=("times new roman", 20, "bold"), bg="grey")
        developer_label.place(x=10, y=280)

        
if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()