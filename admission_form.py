


"""2026"""
import customtkinter as ctk
from tkinter import messagebox
from reportlab.pdfgen import canvas
import pymysql
import os
import platform
import subprocess
import random

# Helper to open PDF
def open_pdf(file_path):
    if platform.system() == "Windows":
        os.startfile(file_path)
    elif platform.system() == "Darwin":
        subprocess.call(["open", file_path])
    else:
        subprocess.call(["xdg-open", file_path])

class AdmissionForm:
    def __init__(self, root):
        self.root = root
        self.root.title("CAP Admission Form")
        self.root.geometry("700x700")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(self.frame, text="CAP ROUND FORM", font=("Arial", 24, "bold")).pack(pady=20)

        # Form fields
        self.name_entry = ctk.CTkEntry(self.frame, placeholder_text="Full Name")
        self.category_entry = ctk.CTkEntry(self.frame, placeholder_text="Category")
        self.gender_entry = ctk.CTkEntry(self.frame, placeholder_text="Gender")
        self.ews_entry = ctk.CTkEntry(self.frame, placeholder_text="EWS Status (Yes/No)")

        self.name_entry.pack(pady=5)
        self.category_entry.pack(pady=5)
        self.gender_entry.pack(pady=5)
        self.ews_entry.pack(pady=5)

        # Generate DSD number
        self.dsd = "DSD" + str(random.randint(10000, 99999))
        self.dsd_label = ctk.CTkLabel(self.frame, text=f"Generated DSD No: {self.dsd}", text_color="gray")
        self.dsd_label.pack(pady=5)

        # Multi-select courses
        ctk.CTkLabel(self.frame, text="Select Preferred Courses").pack(pady=5)
        self.course_options = ["Computer Science", "Mechanical", "Civil", "Electrical", "AI & ML", "IT"]
        self.course_box = ctk.CTkComboBox(self.frame, values=self.course_options, state="readonly")
        self.course_box.pack(pady=5)
        self.selected_courses = []

        add_course_btn = ctk.CTkButton(self.frame, text="Add Course", command=self.add_course)
        add_course_btn.pack(pady=2)

        self.course_list_label = ctk.CTkLabel(self.frame, text="Selected Courses: None")
        self.course_list_label.pack(pady=5)

        # Multi-select colleges
        ctk.CTkLabel(self.frame, text="Select Preferred Colleges").pack(pady=5)
        self.college_options = ["K.K. Wagh", "MET", "Guru Gobind Singh", "KVN", "Sandip", "Sapkal"]
        self.college_box = ctk.CTkComboBox(self.frame, values=self.college_options, state="readonly")
        self.college_box.pack(pady=5)
        self.selected_colleges = []

        add_college_btn = ctk.CTkButton(self.frame, text="Add College", command=self.add_college)
        add_college_btn.pack(pady=2)

        self.college_list_label = ctk.CTkLabel(self.frame, text="Selected Colleges: None")
        self.college_list_label.pack(pady=5)

        # Submit button
        submit_btn = ctk.CTkButton(self.frame, text="Submit", command=self.submit_form)
        submit_btn.pack(pady=20)

        # View Admission Schedule PDF button
        view_schedule_btn = ctk.CTkButton(self.frame, text="View Admission Schedule", command=self.view_schedule)
        view_schedule_btn.pack(pady=5)

    def add_course(self):
        course = self.course_box.get()
        if course and course not in self.selected_courses:
            self.selected_courses.append(course)
            self.course_list_label.configure(text="Selected Courses: " + ", ".join(self.selected_courses))

    def add_college(self):
        college = self.college_box.get()
        if college and college not in self.selected_colleges:
            self.selected_colleges.append(college)
            self.college_list_label.configure(text="Selected Colleges: " + ", ".join(self.selected_colleges))

    def submit_form(self):
        name = self.name_entry.get()
        dsd = self.dsd
        category = self.category_entry.get()
        gender = self.gender_entry.get()
        ews = self.ews_entry.get()
        courses = ", ".join(self.selected_courses)
        colleges = ", ".join(self.selected_colleges)

        if not all([name, category, gender, ews]) or not courses or not colleges:
            messagebox.showerror("Error", "All fields are required and selections must be made.")
            return

        try:
            # Update database credentials as per your local setup
            con = pymysql.connect(host="localhost", user="root", password="", database="dsy")
            cur = con.cursor()
            cur.execute("INSERT INTO admission (name, dsdno, category, gender, ews, courses, colleges) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                        (name, dsd, category, gender, ews, courses, colleges))
            con.commit()
            cur.close()
            con.close()
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not save to database: {e}")
            return

        self.generate_pdf(name, dsd, category, gender, ews, courses, colleges)
        messagebox.showinfo("Success", "Admission form submitted successfully!")

    def generate_pdf(self, name, dsd, category, gender, ews, courses, colleges):
        filename = f"AdmissionForm_{dsd}.pdf"
        c = canvas.Canvas(filename)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(180, 800, "Guru Gobind Singh College - CAP Round Admission Form")
        c.setFont("Helvetica", 12)

        c.drawString(100, 750, f"Name: {name}")
        c.drawString(100, 730, f"DSD No: {dsd}")
        c.drawString(100, 710, f"Category: {category}")
        c.drawString(100, 690, f"Gender: {gender}")
        c.drawString(100, 670, f"EWS: {ews}")
        c.drawString(100, 650, f"Selected Courses: {courses}")
        c.drawString(100, 630, f"Preferred Colleges: {colleges}")

        c.save()
        open_pdf(filename)

    def view_schedule(self):
        pdf_path = "Admission_Schedule_Details.pdf"
        if os.path.exists(pdf_path):
            open_pdf(pdf_path)
        else:
            messagebox.showerror("Error", "Admission Schedule PDF not found.")

def launch_admission_form():
    root = ctk.CTk()
    app = AdmissionForm(root)
    root.mainloop()

if __name__ == "__main__":
    launch_admission_form()



