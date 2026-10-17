from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk")

        title_lbl = Label(
            self.root,
            text="HELP  DESK",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="blue",
        )
        title_lbl.place(x=0, y=0, width=1536, height=45)
        help_img = Image.open(r"E:\face recognisation model\potos\hellp.png")
        help_img = help_img.resize((1536, 1024), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(help_img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=45, width=1530, height=1024)



if __name__ == "__main__":
    root = Tk()
    obj = help(root)
    root.mainloop()
