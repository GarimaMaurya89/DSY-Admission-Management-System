import customtkinter as ctk
import pymysql
from tkinter import messagebox

class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard - Manage Applications")
        self.root.geometry("1100x750")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(self.frame, text="Admin Dashboard - Admission Applications", font=("Arial", 22, "bold")).pack(pady=10)

        # ------------------ Textbox ------------------
        self.textbox = ctk.CTkTextbox(self.frame, width=1050, height=400, font=("Consolas", 12))
        self.textbox.pack(pady=10)

        # ------------------ Button Frame ------------------
        btn_frame = ctk.CTkFrame(self.frame)
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="Refresh Records", command=self.load_data, width=170).grid(row=0, column=0, padx=10)
        ctk.CTkButton(btn_frame, text="Delete Record", command=self.delete_record, width=170, fg_color="red").grid(row=0, column=1, padx=10)
        ctk.CTkButton(btn_frame, text="Update Record", command=self.update_record, width=170, fg_color="green").grid(row=0, column=2, padx=10)

        # ------------------ Search Section ------------------
        search_frame = ctk.CTkFrame(self.frame)
        search_frame.pack(pady=10)

        ctk.CTkLabel(search_frame, text="Search by College:").grid(row=0, column=0, padx=5)
        self.search_entry = ctk.CTkEntry(search_frame, width=250, placeholder_text="Enter college name (e.g., KKW)")
        self.search_entry.grid(row=0, column=1, padx=5)

        ctk.CTkButton(search_frame, text="Search", command=self.search_college, width=150).grid(row=0, column=2, padx=10)

        # ------------------ Entry Fields for Update/Delete ------------------
        entry_frame = ctk.CTkFrame(self.frame)
        entry_frame.pack(pady=15)

        ctk.CTkLabel(entry_frame, text="Enter DSD No:").grid(row=0, column=0, padx=5)
        self.dsd_entry = ctk.CTkEntry(entry_frame, width=150)
        self.dsd_entry.grid(row=0, column=1, padx=5)

        ctk.CTkLabel(entry_frame, text="Name:").grid(row=0, column=2, padx=5)
        self.name_entry = ctk.CTkEntry(entry_frame, width=150)
        self.name_entry.grid(row=0, column=3, padx=5)

        ctk.CTkLabel(entry_frame, text="Category:").grid(row=0, column=4, padx=5)
        self.category_entry = ctk.CTkEntry(entry_frame, width=150)
        self.category_entry.grid(row=0, column=5, padx=5)

        ctk.CTkLabel(entry_frame, text="Gender:").grid(row=1, column=0, padx=5, pady=5)
        self.gender_entry = ctk.CTkEntry(entry_frame, width=150)
        self.gender_entry.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(entry_frame, text="EWS:").grid(row=1, column=2, padx=5, pady=5)
        self.ews_entry = ctk.CTkEntry(entry_frame, width=150)
        self.ews_entry.grid(row=1, column=3, padx=5, pady=5)

        ctk.CTkLabel(entry_frame, text="Courses:").grid(row=1, column=4, padx=5, pady=5)
        self.courses_entry = ctk.CTkEntry(entry_frame, width=150)
        self.courses_entry.grid(row=1, column=5, padx=5, pady=5)

        ctk.CTkLabel(entry_frame, text="Colleges:").grid(row=2, column=0, padx=5, pady=5)
        self.colleges_entry = ctk.CTkEntry(entry_frame, width=400)
        self.colleges_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        self.load_data()

    # ------------------ Load Data ------------------
    def load_data(self):
        self.textbox.delete("1.0", "end")
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="dsy")
            cur = con.cursor()
            cur.execute("SELECT * FROM admission")
            records = cur.fetchall()
            cur.close()
            con.close()

            self.display_records(records)

        except Exception as e:
            messagebox.showerror("Database Error", f"Could not retrieve data: {e}")

    # ------------------ Display Records ------------------
    def display_records(self, records):
        self.textbox.delete("1.0", "end")
        if not records:
            self.textbox.insert("end", "No applicants found.")
            return

        header = f"{'Name':<20}{'DSD No':<15}{'Category':<15}{'Gender':<10}{'EWS':<8}{'Courses':<25}{'Colleges':<30}\n"
        self.textbox.insert("end", header)
        self.textbox.insert("end", "="*120 + "\n")

        for row in records:
            name, dsdno, category, gender, ews, courses, colleges = row
            line = f"{name:<20}{dsdno:<15}{category:<15}{gender:<10}{ews:<8}{courses[:25]:<25}{colleges[:30]:<30}\n"
            self.textbox.insert("end", line)

    # ------------------ Search College ------------------
    def search_college(self):
        search_term = self.search_entry.get().strip()
        if not search_term:
            messagebox.showerror("Error", "Please enter a college name to search.")
            return
        try:
            # Update database credentials as per your local setup
            con = pymysql.connect(host="localhost", user="root", password="", database="dsy")
            cur = con.cursor()
            query = "SELECT * FROM admission WHERE colleges LIKE %s"
            cur.execute(query, (f"%{search_term}%",))
            records = cur.fetchall()
            cur.close()
            con.close()

            if not records:
                messagebox.showinfo("No Results", f"No students found for college: {search_term}")
            else:
                self.display_records(records)

        except Exception as e:
            messagebox.showerror("Database Error", f"Error searching records: {e}")

    # ------------------ Delete Record ------------------
    def delete_record(self):
        dsd = self.dsd_entry.get()
        if not dsd:
            messagebox.showerror("Error", "Please enter DSD No to delete record.")
            return
        try:
            # Update database credentials as per your local setup
            con = pymysql.connect(host="localhost", user="root", password="", database="dsy")
            cur = con.cursor()
            cur.execute("DELETE FROM admission WHERE dsdno=%s", (dsd,))
            con.commit()
            cur.close()
            con.close()
            messagebox.showinfo("Success", f"Record with DSD No {dsd} deleted successfully.")
            self.load_data()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error deleting record: {e}")

    # ------------------ Update Record ------------------
    def update_record(self):
        dsd = self.dsd_entry.get()
        name = self.name_entry.get()
        category = self.category_entry.get()
        gender = self.gender_entry.get()
        ews = self.ews_entry.get()
        courses = self.courses_entry.get()
        colleges = self.colleges_entry.get()

        if not dsd:
            messagebox.showerror("Error", "Please enter DSD No to update record.")
            return

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="dsy")
            cur = con.cursor()
            cur.execute("""
                UPDATE admission 
                SET name=%s, category=%s, gender=%s, ews=%s, courses=%s, colleges=%s 
                WHERE dsdno=%s
            """, (name, category, gender, ews, courses, colleges, dsd))
            con.commit()
            cur.close()
            con.close()
            messagebox.showinfo("Success", f"Record with DSD No {dsd} updated successfully.")
            self.load_data()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error updating record: {e}")


# ------------------ Launch ------------------
def launch():
    root = ctk.CTk()
    app = AdminDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    launch()


