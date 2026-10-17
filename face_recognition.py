from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import csv # Added for cleaner CSV handling

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION ", font=("times new roman", 35, "bold"),
                          bg="white", fg="Goldenrod")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # first image
        img_top = Image.open(r"potos\facedetect.png")
        img_top = img_top.resize((650, 735), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl3 = Label(self.root, image=self.photoimg_top)
        f_lbl3.place(x=0, y=55, width=650, height=735)

        # second image
        img_bottom = Image.open(r"potos\facedetect2.png")
        img_bottom = img_bottom.resize((950, 735), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl4 = Label(self.root, image=self.photoimg_bottom)
        f_lbl4.place(x=650, y=55, width=950, height=735)

        # button
        b1_1 = Button(self.root, text="Face Recognition", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 20, "bold"), bg="dark green", fg="white")
        b1_1.place(x=975, y=710, width=340, height=40)

    # --- CORRECTED: mark_attendance defined as a proper class method ---
    def mark_attendance(self, roll, name, class_name):
        """Logs attendance to a CSV file if the roll number has not been logged today."""
        
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:%S")

        try:
            with open("schoolattendance.csv", "a+", newline="") as f:
                f.seek(0)
                reader = csv.reader(f)
                myDataList = list(reader)

                if not myDataList or not myDataList[0][0].lower() == 'roll':
                    writer = csv.writer(f)
                    writer.writerow(["Roll", "Name", "Class", "Time", "Date"])
                    myDataList = list(csv.reader(open("schoolattendance.csv", "r")))

                already_marked = False
                for row in myDataList:
                    if len(row) >= 5 and row[0].strip() == str(roll).strip() and row[4].strip() == current_date:
                        already_marked = True
                        break

                if not already_marked:
                    writer = csv.writer(f)
                    writer.writerow([roll, name, class_name, dtString, current_date])
                    print(f"ATTENDANCE MARKED: Roll: {roll}, Name: {name}")

        except Exception as e:
            messagebox.showerror("Attendance Error", f"Could not log attendance: {e}", parent=self.root)


    def face_recog(self):
        
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            conn = None
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                n, c, r = "Unknown", "Unknown", str(id)

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Vkd55555##",
                        database="student"
                    )

                    # FIX 1 — buffered cursor
                    my_cursor = conn.cursor(buffered=True)

                    my_cursor.execute("SELECT name, class, roll FROM attendance WHERE roll=%s", (id,))
                    result = my_cursor.fetchone()

                    # FIX 2 — clear remaining unread results
                    my_cursor.fetchall()

                    if result:
                        n, c, r = result

                except mysql.connector.Error as err:
                    print(f"Database Error: {err}")
                finally:
                    if conn and conn.is_connected():
                        conn.close()

                if confidence > 77:
                    self.mark_attendance(r, n, c)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Class:{c}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        try:
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")
        except Exception as e:
            messagebox.showerror("Setup Error", f"Missing files or setup issue: {e}", parent=self.root)
            return

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13 or cv2.waitKey(1) == ord('q'):
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
