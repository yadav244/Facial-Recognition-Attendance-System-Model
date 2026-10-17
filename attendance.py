from pdb import main
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_attendance_id = StringVar()
        self.var_name = StringVar()
        self.var_class = StringVar()
        self.var_roll = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_status = StringVar()


        #first image
        img_top = Image.open(r"potos\Attendance left.png")
        img_top = img_top.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl3 = Label(self.root, image=self.photoimg_top)
        f_lbl3.place(x=0, y=0, width=800, height=200)

        #second image
        img_bottom = Image.open(r"potos\Attendance right.jpg")
        img_bottom = img_bottom.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl4 = Label(self.root, image=self.photoimg_bottom)
        f_lbl4.place(x=800, y=0, width=800, height=200)

        # background image
        img4 = Image.open(r"potos\background.jpg")
        img4 = img4.resize((1530, 590), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1530, height=590)
        title_lbl = Label(bg_img, text="ATTENDANCE  MANAGEMENT  SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="Purple")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1485, height=520)
        
        #left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=500)

        img_left = Image.open(r"potos\frame left.jpg")
        img_left = img_left.resize((720, 400), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=200)

        left_inside_frame = Frame(Left_frame, bd=2, bg="white", relief=RIDGE)
        left_inside_frame.place(x=5, y=210, width=720, height=280)

        #label and entry
        attendance_frame = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white")
        attendance_frame.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        attendance_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_attendance_id, font=("times new roman", 12, "bold"))
        attendance_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        #name
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        name_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_name, font=("times new roman", 12, "bold"))
        name_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        #class
        class_label = Label(left_inside_frame, text="Class:", font=("times new roman", 12, "bold"), bg="white")
        class_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_class, font=("times new roman", 12, "bold"), width=18, state="readonly")
        class_combo["values"] = ("Select Class", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII")
        class_combo.current(0)
        class_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        #ROLL NO
        roll_label = Label(left_inside_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        roll_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_roll, font=("times new roman", 12, "bold"))
        roll_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        #DATE
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        date_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_date, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        #TIME
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        time_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_time, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        #attendance status
        attendance_status_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        attendance_status_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        attendance_status_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_status, font=("times new roman", 12, "bold"), width=18,  state="readonly")
        attendance_status_combo["values"] = ("Select Status", "Present", "Absent")
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        #button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=220, width=690, height=35)

        save_btn = Button(btn_frame, text="Import CSV",command=self.importCsv, width=18, font=("times new roman", 12, "bold"), bg="Dark Green", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export CSV", command=self.exportCsv, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=18, font=("times new roman", 12, "bold"), bg="purple", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=18, font=("times new roman", 12, "bold"), bg="dark red", fg="white")
        reset_btn.grid(row=0, column=3)

        #right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance  Details  Table", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=500)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=0, width=710, height=470)
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.attendance_table = ttk.Treeview(table_frame, column=("attendanceid", "name", "class", "roll", "date", "time", "status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)
        self.attendance_table.heading("attendanceid", text="Attendance ID")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("class", text="Class")
        self.attendance_table.heading("roll", text="Roll No")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("status", text="Status")
        self.attendance_table["show"] = "headings"
        self.attendance_table.column("attendanceid", width=100)
        self.attendance_table.column("name", width=100) 
        self.attendance_table.column("class", width=100)
        self.attendance_table.column("roll", width=100)
        self.attendance_table.column("date", width=100)
        self.attendance_table.column("time", width=100)
        self.attendance_table.column("status", width=100)
        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)

        #fetch data
    def fetchData(self, rows):
        self.attendance_table.delete(*self.attendance_table. get_children())
        for i in rows:
            self.attendance_table.insert("", END, values=i)
#import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            #export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported", "Your data exported to " + os.path.basename(fln) + " successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_row)
        row = content["values"]
        self.var_attendance_id.set(row[0])
        self.var_name.set(row[1])
        self.var_class.set(row[2])
        self.var_roll.set(row[3])
        self.var_date.set(row[4])
        self.var_time.set(row[5])
        self.var_status.set(row[6])

        #reset
    def reset_data(self):
        self.var_attendance_id.set("")
        self.var_name.set("")
        self.var_class.set("Select Class")
        self.var_roll.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_status.set("Select Status")




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()