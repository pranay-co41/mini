import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    length = int(length_entry.get())

    char_set = ""
    if var_upper.get():
        char_set += string.ascii_uppercase
    if var_lower.get():
        char_set += string.ascii_lowercase
    if var_numbers.get():
        char_set += string.digits
    if var_symbols.get():
        char_set += string.punctuation

    if not char_set:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    password = ''.join(random.choices(char_set, k=length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x400")
root.resizable(False, False)

# Title
tk.Label(root, text="🔐 Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

# Password length
tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack(pady=5)

# Checkboxes
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack(anchor='w', padx=20)

# Output field
password_var = tk.StringVar()
tk.Label(root, text="Generated Password:").pack(pady=10)
tk.Entry(root, textvariable=password_var, font=("Courier", 12), width=30, justify='center').pack()

# Buttons
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

root.mainloop()
