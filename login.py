import customtkinter as ctk
from tkinter import messagebox
from dashboard_student import StudentDashboard
from dashboard_admin import AdminDashboard

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Login | Smart Admission System")

        self.frame = ctk.CTkFrame(master=root)
        self.frame.pack(pady=60, padx=60, fill="both", expand=True)

        self.title = ctk.CTkLabel(master=self.frame, text="Login Portal", font=("Arial", 24, "bold"))
        self.title.pack(pady=20)

        self.user_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Username")
        self.user_entry.pack(pady=10)

        self.pass_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.pass_entry.pack(pady=10)

        self.role_menu = ctk.CTkOptionMenu(master=self.frame, values=["Student", "Admin"])
        self.role_menu.pack(pady=10)

        self.login_btn = ctk.CTkButton(master=self.frame, text="Login", command=self.login)
        self.login_btn.pack(pady=20)

    def login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        role = self.role_menu.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        if role == "Student":
            if username == "student" and password == "1234":
                self.open_student_dashboard()
            else:
                messagebox.showerror("Error", "Invalid student credentials", parent=self.root)
        elif role == "Admin":
            if username == "admin" and password == "admin123":
                self.open_admin_dashboard()
            else:
                messagebox.showerror("Error", "Invalid admin credentials", parent=self.root)

    def open_student_dashboard(self):
        self.root.destroy()
        import dashboard_student
        dashboard_student.launch()


    def open_admin_dashboard(self):
        self.root.destroy()
        import dashboard_admin
        dashboard_admin.launch()


if __name__ == "__main__":
    root = ctk.CTk()
    app = LoginApp(root)
    root.mainloop()


    
"""import customtkinter as ctk
from tkinter import messagebox
from dashboard_student import StudentDashboard
from dashboard_admin import AdminDashboard

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Login | Smart Admission System")

        self.frame = ctk.CTkFrame(master=root)
        self.frame.pack(pady=60, padx=60, fill="both", expand=True)

        self.title = ctk.CTkLabel(
            master=self.frame,
            text="Login Portal",
            font=("Arial", 24, "bold")
        )
        self.title.pack(pady=20)

        self.user_entry = ctk.CTkEntry(
            master=self.frame,
            placeholder_text="Username"
        )
        self.user_entry.pack(pady=10)

        self.pass_entry = ctk.CTkEntry(
            master=self.frame,
            placeholder_text="Password",
            show="*"
        )
        self.pass_entry.pack(pady=10)

        self.role_menu = ctk.CTkOptionMenu(
            master=self.frame,
            values=["Student", "Admin"]
        )
        self.role_menu.pack(pady=10)

        self.login_btn = ctk.CTkButton(
            master=self.frame,
            text="Login",
            command=self.login
        )
        self.login_btn.pack(pady=20)

    # ---------------- LOGIN LOGIC ----------------
    def login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        role = self.role_menu.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        # ---- STUDENT LOGIN ----
        if role == "Student":
            if username == "student" and password == "1234":
                dsd_no = "DSD2025001"   # (Later fetch from DB)
                self.open_student_dashboard(dsd_no)
            else:
                messagebox.showerror("Error", "Invalid student credentials", parent=self.root)

        # ---- ADMIN LOGIN ----
        elif role == "Admin":
            if username == "admin" and password == "admin123":
                self.open_admin_dashboard()
            else:
                messagebox.showerror("Error", "Invalid admin credentials", parent=self.root)

    # ---------------- STUDENT DASHBOARD ----------------
    def open_student_dashboard(self, dsd_no):
        self.root.destroy()
        dash = ctk.CTk()
        StudentDashboard(dash, dsd_no)
        dash.mainloop()

    # ---------------- ADMIN DASHBOARD ----------------
    def open_admin_dashboard(self):
        self.root.destroy()
        dash = ctk.CTk()
        AdminDashboard(dash)
        dash.mainloop()


# ---------------- APP START ----------------
if __name__ == "__main__":
    root = ctk.CTk()
    app = LoginApp(root)
    root.mainloop()"""