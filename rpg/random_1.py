import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


def generate_password():
    length = password_length.get()

   
    include_upper = uppercase_var.get()
    include_lower = lowercase_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    if not (include_upper or include_lower or include_digits or include_special):
        messagebox.showerror("Error", "Please select at least one character type!")
        return

    chars = ""
    if include_upper:
        chars += string.ascii_uppercase
    if include_lower:
        chars += string.ascii_lowercase
    if include_digits:
        chars += string.digits
    if include_special:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy!")


app = tk.Tk()
app.title("Advanced Password Generator")
app.geometry("400x400")
app.resizable(False, False)


tk.Label(app, text="Password Generator", font=("Arial", 18)).pack(pady=10)


tk.Label(app, text="Select Password Length:", font=("Arial", 12)).pack(pady=5)
password_length = tk.IntVar(value=12)
length_slider = tk.Scale(app, from_=8, to_=32, orient="horizontal", variable=password_length)
length_slider.pack(pady=5)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(app, text="Include Uppercase Letters (A-Z)", variable=uppercase_var).pack(anchor="w", padx=20)
tk.Checkbutton(app, text="Include Lowercase Letters (a-z)", variable=lowercase_var).pack(anchor="w", padx=20)
tk.Checkbutton(app, text="Include Digits (0-9)", variable=digits_var).pack(anchor="w", padx=20)
tk.Checkbutton(app, text="Include Special Characters (!@#$%^&*)", variable=special_var).pack(anchor="w", padx=20)


password_entry = tk.Entry(app, font=("Arial", 12), width=30)
password_entry.pack(pady=10)


generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)


copy_button = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)


app.mainloop()
