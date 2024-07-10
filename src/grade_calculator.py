import tkinter as tk
from tkinter import messagebox

class GradeCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grade Calculator")
        self.geometry("800x400")
        
        self.subject_count_label = tk.Label(self, text="Enter number of subjects completed:")
        self.subject_count_label.pack()
        
        self.subject_count_entry = tk.Entry(self)
        self.subject_count_entry.pack()
        
        self.submit_count_button = tk.Button(self, text="Submit", command=self.create_subject_entries)
        self.submit_count_button.pack()
        
        self.subject_entries_frame = tk.Frame(self)
        self.subject_entries_frame.pack()
        
        self.calculate_button = tk.Button(self, text="Calculate Grade", command=self.calculate_grade)
        self.calculate_button.pack()
        
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
        
    def create_subject_entries(self):
        for widget in self.subject_entries_frame.winfo_children():
            widget.destroy()
        
        try:
            self.subject_count = int(self.subject_count_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of subjects.")
            return
        
        self.subject_entries = []
        for i in range(self.subject_count):
            label = tk.Label(self.subject_entries_frame, text=f"Subject {i+1} Grade:")
            label.grid(row=i, column=0)
            entry = tk.Entry(self.subject_entries_frame)
            entry.grid(row=i, column=1)
            ects_label = tk.Label(self.subject_entries_frame, text="ECTS:")
            ects_label.grid(row=i, column=2)
            ects_entry = tk.Entry(self.subject_entries_frame)
            ects_entry.grid(row=i, column=3)
            scale_label = tk.Label(self.subject_entries_frame, text="Scale (e.g., 30, 50, 100):")
            scale_label.grid(row=i, column=4)
            scale_entry = tk.Entry(self.subject_entries_frame)
            scale_entry.grid(row=i, column=5)
            self.subject_entries.append((entry, ects_entry, scale_entry))
    
    def calculate_grade(self):
        total_weighted_grade = 0
        total_ects = 0
        
        for grade_entry, ects_entry, scale_entry in self.subject_entries:
            try:
                grade = float(grade_entry.get())
                ects = float(ects_entry.get())
                scale = float(scale_entry.get())
                
                # Normalize the grade to a 100 scale
                normalized_grade = (grade / scale) * 100
                
                total_weighted_grade += normalized_grade * ects
                total_ects += ects
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid grades, ECTS, and scales.")
                return
        
        if total_ects == 0:
            messagebox.showerror("Invalid Input", "Total ECTS cannot be zero.")
            return
        
        final_grade_100 = total_weighted_grade / total_ects
        final_grade_10 = final_grade_100 / 10
        
        self.result_label.config(text=f"Approximate Final Grade: {final_grade_100:.2f} (out of 100), {final_grade_10:.2f} (out of 10)")

if __name__ == "__main__":
    app = GradeCalculator()
    app.mainloop()
