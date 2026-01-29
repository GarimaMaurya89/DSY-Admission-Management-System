import customtkinter as ctk
from tkinter import messagebox
import pymysql


class RegisterForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration")
        self.root.geometry("600x500")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(self.frame, text="Student Registration", font=("Arial", 24, "bold")).pack(pady=20)

        self.name_entry = ctk.CTkEntry(self.frame, placeholder_text="Full Name")
        self.phoneno_entry = ctk.CTkEntry(self.frame, placeholder_text="Phone Number")
        self.adddress_entry = ctk.CTkEntry(self.frame, placeholder_text="Address")
        self.email_entry = ctk.CTkEntry(self.frame, placeholder_text="Email")
        self.category_entry = ctk.CTkEntry(self.frame, placeholder_text="Category")
        self.sscmarksentry = ctk.CTkEntry(self.frame, placeholder_text="SSC Marks")
        self.hscmarksentry = ctk.CTkEntry(self.frame, placeholder_text="HSC Marks")

        for entry in [self.name_entry, self.phoneno_entry, self.adddress_entry, self.email_entry,
                      self.category_entry, self.sscmarksentry, self.hscmarksentry]:
            entry.pack(pady=5)

        submit_btn = ctk.CTkButton(self.frame, text="Register", command=self.register)
        submit_btn.pack(pady=20)

    def register(self):
        data = {
            "name": self.name_entry.get(),
            "phoneno": self.phoneno_entry.get(),
            "adddress": self.adddress_entry.get(),
            "email": self.email_entry.get(),
            "category": self.category_entry.get(),
            "sscmarks": self.sscmarksentry.get(),
            "hscmarks": self.hscmarksentry.get()
        }

        if any(v == "" for v in data.values()):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            # Update database credentials as per your local setup
            con = pymysql.connect(host="localhost", user="root", password="", database="student")
            cur = con.cursor()
            cur.execute("INSERT INTO stud (name, phoneno, adddress, email, category, sscmarks, hscmarks) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (data["name"], data["phoneno"], data["adddress"], data["email"], data["category"], data["sscmarks"], data["hscmarks"]))
            con.commit()
            cur.close()
            con.close()
            messagebox.showinfo("Success", "Registration successful! Proceed to CAP form.", parent=self.root)

            self.root.destroy()
            

        except Exception as e:
            messagebox.showerror("Database Error", f"Could not save to database: {e}", parent=self.root)


def launch_register():
    root = ctk.CTk()
    app = RegisterForm(root)
    root.mainloop()


if __name__ == "__main__":
    launch_register()


# register.py
"""import customtkinter as ctk
from tkinter import messagebox
import pymysql
import admission_form  # will open after registration

def launch_register():
    root = ctk.CTk()
    app = RegisterForm(root)
    root.mainloop()

class RegisterForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration")
        self.root.geometry("500x500")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(self.frame, text="Student Registration", font=("Arial", 20)).pack(pady=10)

        self.name_entry = ctk.CTkEntry(self.frame, placeholder_text="Full Name")
        self.phone_entry = ctk.CTkEntry(self.frame, placeholder_text="Phone Number")
        self.address_entry = ctk.CTkEntry(self.frame, placeholder_text="Address")
        self.email_entry = ctk.CTkEntry(self.frame, placeholder_text="Email")
        self.category_entry = ctk.CTkEntry(self.frame, placeholder_text="Category")
        self.ssc_entry = ctk.CTkEntry(self.frame, placeholder_text="SSC Marks")
        self.hsc_entry = ctk.CTkEntry(self.frame, placeholder_text="HSC Marks")

        for entry in [self.name_entry, self.phone_entry, self.address_entry, self.email_entry,
                      self.category_entry, self.ssc_entry, self.hsc_entry]:
            entry.pack(pady=5)

        ctk.CTkButton(self.frame, text="Register", command=self.register).pack(pady=20)

    def register(self):
        data = {
            "name": self.name_entry.get(),
            "phone": self.phone_entry.get(),
            "address": self.address_entry.get(),
            "email": self.email_entry.get(),
            "category": self.category_entry.get(),
            "ssc": self.ssc_entry.get(),
            "hsc": self.hsc_entry.get()
        }

        if any(v == "" for v in data.values()):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="student")
            cur = con.cursor()
            cur.execute("INSERT INTO stud (name, phoneno, address, email, category, ssc_marks, hsc_marks) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                        (data["name"], data["phone"], data["address"], data["email"], data["category"], data["ssc"], data["hsc"]))
            con.commit()
            con.close()

            messagebox.showinfo("Success", "Registered Successfully! Proceeding to CAP Form.", parent=self.root)
            self.root.destroy()
            admission_form.launch_admission_form()

        except Exception as e:
            messagebox.showerror("Database Error", f"Could not register: {e}", parent=self.root)"""
    