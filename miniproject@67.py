import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        name = name_entry.get()
        age = int(age_entry.get())
        gender = gender_var.get()
        height_cm = float(height_entry.get())
        weight_kg = float(weight_entry.get())

        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result = (
            f"Name: {name}\n"
            f"Age: {age}\n"
            f"Gender: {gender}\n"
            f"BMI: {bmi:.2f}\n"
            f"Category: {category}"
        )

        messagebox.showinfo("BMI Result", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for age, height, and weight.")

# GUI Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x350")
root.resizable(False, False)

# Labels and Entries
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Gender:").pack()
gender_var = tk.StringVar()
gender_var.set("Select")
tk.OptionMenu(root, gender_var, "Male", "Female", "Other").pack()

tk.Label(root, text="Height (cm):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

root.mainloop()
