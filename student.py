from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ================== Variables ==================
        self.var_class = StringVar()
        self.var_section = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_father = StringVar()
        self.var_mother = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_class_teacher = StringVar()
        self.var_radio1 = StringVar()
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        # ================== Top Images ==================
        try:
            img = Image.open(r"E:\face recognisation model\potos\students1.jpeg")
            img = img.resize((500, 130), Image.Resampling.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)
            f_lbl = Label(self.root, image=self.photoimg)
            f_lbl.place(x=0, y=0, width=500, height=130)

            img2 = Image.open(r"E:\face recognisation model\potos\students2.jpeg")
            img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
            f_lbl2 = Label(self.root, image=self.photoimg2)
            f_lbl2.place(x=500, y=0, width=500, height=130)

            img3 = Image.open(r"E:\face recognisation model\potos\students3.jpeg")
            img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)
            f_lbl3 = Label(self.root, image=self.photoimg3)
            f_lbl3.place(x=1000, y=0, width=500, height=130)
        except FileNotFoundError:
            messagebox.showerror("Error", "Image files not found. Please check the paths.", parent=self.root)

        # ================== Background ==================
        try:
            img4 = Image.open(r"E:\face recognisation model\potos\imaage4.jpg")
            img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)
            self.photoimg4 = ImageTk.PhotoImage(img4)
            bg_img = Label(self.root, image=self.photoimg4)
            bg_img.place(x=0, y=130, width=1530, height=710)
        except FileNotFoundError:
            messagebox.showerror("Error", "Background image file not found. Please check the path.", parent=self.root)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=50, width=1500, height=600)

        # ================== Left Frame ==================
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=760, height=580)

        try:
            img_left = Image.open(r"E:\face recognisation model\potos\leftimage.jpg")
            img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)
            f_lbl3 = Label(left_frame, image=self.photoimg_left)
            f_lbl3.place(x=5, y=-5, width=720, height=150)
        except FileNotFoundError:
            messagebox.showerror("Error", "Left frame image not found. Please check the path.", parent=self.root)

        # ================== Current Course ==================
        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Current Course Information",
                                          font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=60)

        dep_label = Label(current_course_frame, text="Class:", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_class,
                                 font=("times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Class", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # ================== Class Student Info ==================
        class_student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Class Student Information",
                                         font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=195, width=720, height=350)

        # Student Name
        student_name_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"))
        student_name_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_name, width=20,
                                       font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(class_student_frame, text="Roll No:", font=("times new roman", 12, "bold"))
        roll_no_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20,
                                  font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Section
        section_label = Label(class_student_frame, text="Section:", font=("times new roman", 12, "bold"))
        section_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        section_combo = ttk.Combobox(class_student_frame, textvariable=self.var_section,
                                     font=("times new roman", 12, "bold"), state="readonly", width=18)
        section_combo["values"] = ("Select Section", "A", "B", "C", "D", "E")
        section_combo.current(0)
        section_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"))
        gender_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,
                                    font=("times new roman", 12, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Select Gender", "Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # D.O.B
        dob_label = Label(class_student_frame, text="D.O.B:", font=("times new roman", 12, "bold"))
        dob_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20,
                              font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Father's Name
        father_name_label = Label(class_student_frame, text="Father's Name:", font=("times new roman", 12, "bold"))
        father_name_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        father_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_father, width=20,
                                      font=("times new roman", 12, "bold"))
        father_name_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Mother's Name
        mother_name_label = Label(class_student_frame, text="Mother's Name:", font=("times new roman", 12, "bold"))
        mother_name_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        mother_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_mother, width=20,
                                      font=("times new roman", 12, "bold"))
        mother_name_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        phone_no_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 12, "bold"))
        phone_no_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        phone_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20,
                                   font=("times new roman", 12, "bold"))
        phone_no_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"))
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20,
                                  font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Class Teacher's Name
        class_teacher_name_label = Label(class_student_frame, text="Class Teacher's Name:",
                                         font=("times new roman", 12, "bold"))
        class_teacher_name_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        class_teacher_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_class_teacher, width=20,
                                             font=("times new roman", 12, "bold"))
        class_teacher_name_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons
        radiobtn1 = Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample",
                                value="Yes", font=("times new roman", 12, "bold"))
        radiobtn1.grid(row=5, column=0)
        radiobtn2 = Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample",
                                value="No", font=("times new roman", 12, "bold"))
        radiobtn2.grid(row=5, column=2)

        # Buttons Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=215, width=715, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=19,
                          font=("times new roman", 12, "bold"), bg="green", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=19,
                            font=("times new roman", 12, "bold"), bg="dark blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=19,
                            font=("times new roman", 12, "bold"), bg="red", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=19,
                           font=("times new roman", 12, "bold"), bg="orange", fg="white")
        reset_btn.grid(row=0, column=3)

        
        # Photo Sample Buttons
        btn_frame2 = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame2.place(x=0, y=250, width=715, height=35)

        take_photo_btn = Button(btn_frame2, command=self.generate_dataset,text="Take Photo Sample", width=39,
                                 font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame2, text="Update Photo Sample", width=39,
                                  font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)


        # ================== Right Frame ==================
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=780, y=10, width=700, height=580)
        
        try:
            img_right = Image.open(r"E:\face recognisation model\potos\rightimage.png")
            img_right = img_right.resize((690, 150), Image.Resampling.LANCZOS)
            self.photoimg_right = ImageTk.PhotoImage(img_right)
            f_lbl3 = Label(right_frame, image=self.photoimg_right)
            f_lbl3.place(x=5, y=-5, width=690, height=150)
        except FileNotFoundError:
            messagebox.showerror("Error", "Right frame image not found. Please check the path.", parent=self.root)

        # Search System
        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search System",
                                  font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=690, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"),
                             bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, textvariable=self.var_searchby, font=("times new roman", 12, "bold"),
                                    state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, textvariable=self.var_searchtxt, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=12,
                            font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3)

        show_all_btn = Button(search_frame, text="Show All", width=12,
                              font=("times new roman", 12, "bold"), bg="blue", fg="white")
        show_all_btn.grid(row=0, column=4)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=205, width=690, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
                                          columns=("class", "name", "roll", "section", "gender", "dob",
                                                   "father", "mother", "phone", "address", "class_teacher", "photo_sample"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Table headings
        for col in ("class", "name", "roll", "section", "gender", "dob", "father", "mother", "phone", "address", "class_teacher", "photo_sample"):
            self.student_table.heading(col, text=col.capitalize())
            self.student_table.column(col, width=100)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ================== Functions ==================
    def add_data(self):
        if self.var_class.get() == "Select Class" or self.var_name.get() == "" or self.var_roll.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Vkd55555##",
                    database="student"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO attendance (class, name, roll, section, gender, dob, father, mother, phone, address, class_teacher, photo_sample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_class.get(),
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_section.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_father.get(),
                    self.var_mother.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_class_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # fetch data
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Vkd55555##",
                database="student"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from attendance")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Could not fetch data from database: {str(es)}", parent=self.root)

    # get cursor
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_class.set(data[0])
        self.var_name.set(data[1])
        self.var_roll.set(data[2])
        self.var_section.set(data[3])
        self.var_gender.set(data[4])
        self.var_dob.set(data[5])
        self.var_father.set(data[6])
        self.var_mother.set(data[7])
        self.var_phone.set(data[8])
        self.var_address.set(data[9])
        self.var_class_teacher.set(data[10])
        self.var_radio1.set(data[11])


    # update function
    def update_data(self):
        if self.var_class.get() == "Select Class" or self.var_name.get() == "" or self.var_roll.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Vkd55555##",
                        database="student"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE attendance SET class=%s, name=%s, section=%s, gender=%s, dob=%s, father=%s, mother=%s, phone=%s, address=%s, class_teacher=%s, photo_sample=%s WHERE roll=%s", (
                        self.var_class.get(),
                        self.var_name.get(),
                        self.var_section.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_father.get(),
                        self.var_mother.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_class_teacher.get(),
                        self.var_radio1.get(),
                        self.var_roll.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details have been updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # delete function
    def delete_data(self):
        if self.var_roll.get() == "":
            messagebox.showerror("Error", "Student Roll No must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student details?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Vkd55555##",
                        database="student"
                    )
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM attendance WHERE roll=%s"
                    val = (self.var_roll.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # reset function
    def reset_data(self):
        self.var_class.set("Select Class")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_section.set("Select Section")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_father.set("")
        self.var_mother.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_class_teacher.set("")
        self.var_radio1.set("No")

    # generate data set or take photo sample
    def generate_dataset(self):
        if self.var_class.get() == "Select Class" or self.var_name.get() == "" or self.var_roll.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Update the database
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Vkd55555##",
                    database="student"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE attendance SET class=%s, name=%s, section=%s, gender=%s, dob=%s, father=%s, mother=%s, phone=%s, address=%s, class_teacher=%s, photo_sample=%s WHERE roll=%s", (
                    self.var_class.get(),
                    self.var_name.get(),
                    self.var_section.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_father.get(),
                    self.var_mother.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_class_teacher.get(),
                    self.var_radio1.get(),
                    self.var_roll.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()

                # Load predefined data on face frontals from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # Minimum neighbor = 5
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                
                # Check for 'data' directory and create it if it doesn't exist
                if not os.path.exists("data"):
                    os.makedirs("data")

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, frame = cap.read()
                    if face_cropped(frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/{self.var_roll.get()}_{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        # Add the missing 'org' parameter (position)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                    
                    if cv2.waitKey(1) == 13 or int(img_id) == 200:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
            
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()