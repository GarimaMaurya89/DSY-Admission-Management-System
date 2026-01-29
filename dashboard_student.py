import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def launch_admission_form():
    try:
        subprocess.Popen(["python", "admission_form.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open form.\n{e}")

class StudentDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Dashboard - CAP Admission")
        self.root.geometry("600x400")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(padx=30, pady=30, fill="both", expand=True)

        title = ctk.CTkLabel(master=self.frame, text="Welcome Student", font=("Arial", 24, "bold"))
        title.pack(pady=20)

        cap_btn = ctk.CTkButton(master=self.frame, text="Fill CAP Admission Form", command=launch_admission_form)
        cap_btn.pack(pady=10)

        exit_btn = ctk.CTkButton(master=self.frame, text="Logout", fg_color="red", command=self.root.destroy)
        exit_btn.pack(pady=10)


def launch():
    root = ctk.CTk()
    app = StudentDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    launch()



"""from admission_form import AdmissionForm
import customtkinter as ctk
from tkinter import messagebox


class StudentDashboard:
    def __init__(self, root, dsd_no):
        self.root = root
        self.dsd_no = dsd_no

        self.root.title("Student Dashboard")
        self.root.geometry("600x400")

        frame = ctk.CTkFrame(root)
        frame.pack(padx=30, pady=30, fill="both", expand=True)

        ctk.CTkLabel(
            frame,
            text=f"Welcome Student (DSD: {dsd_no})",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        ctk.CTkButton(
            frame,
            text="Fill Admission Form",
            command=self.open_admission_form
        ).pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Logout",
            fg_color="red",
            command=self.root.destroy
        ).pack(pady=10)

    def open_admission_form(self):
        self.root.destroy()   # close dashboard
        form = ctk.CTk()
        AdmissionForm(form, self.dsd_no)
        form.mainloop()"""