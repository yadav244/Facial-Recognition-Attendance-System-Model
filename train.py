from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"),
                          bg="white", fg="dark red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # top image
        img_top = Image.open(r"potos\traintop.png")
        img_top = img_top.resize((1540, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl3 = Label(self.root, image=self.photoimg_top)
        f_lbl3.place(x=0, y=55, width=1540, height=325)

        # bottom image
        img_bottom = Image.open(r"potos\traindown.jpg")
        img_bottom = img_bottom.resize((1540, 340), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl3 = Label(self.root, image=self.photoimg_bottom)
        f_lbl3.place(x=0, y=450, width=1540, height=340)

                # button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
                      font=("times new roman", 30, "bold"), bg="dark green", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=80)

    
    # Add this method to your class
    def train_classifier(self):
        # Add your face recognition training logic here
        # This function will be called when the button is clicked.
        data_dir = ("data") 
        path= [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            filename = os.path.split(image)[1]     # e.g. "1_1.jpg"
            id = int(filename.split('_')[0])       # takes "1" as ID

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Training", "Training dataSet has been completed.")
        

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()