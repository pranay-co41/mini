import tkinter as tk
from tkinter import messagebox
import random

def generate_otp():
    length = otp_length.get()
    otp = ''.join(random.choices('0123456789', k=length))
    otp_var.set(otp)

def copy_otp():
    root.clipboard_clear()
    root.clipboard_append(otp_var.get())
    messagebox.showinfo("Copied", "OTP copied to clipboard!")

# GUI Window
root = tk.Tk()
root.title("OTP Generator")
root.geometry("300x300")
root.resizable(False, False)

# Title
tk.Label(root, text="🔐 OTP Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

# OTP Length selection
tk.Label(root, text="Select OTP Length:").pack()

otp_length = tk.IntVar(value=6)
tk.Radiobutton(root, text="4 digits", variable=otp_length, value=4).pack()
tk.Radiobutton(root, text="6 digits", variable=otp_length, value=6).pack()
tk.Radiobutton(root, text="8 digits", variable=otp_length, value=8).pack()

# OTP Display
otp_var = tk.StringVar()
tk.Label(root, text="Generated OTP:").pack(pady=10)
tk.Entry(root, textvariable=otp_var, font=("Courier", 14), justify="center").pack()

# Buttons
tk.Button(root, text="Generate OTP", command=generate_otp).pack(pady=10)
tk.Button(root, text="Copy to Clipboard", command=copy_otp).pack()

root.mainloop()
