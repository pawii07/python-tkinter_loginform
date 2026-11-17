import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Form")
root.geometry("400x350")
root.configure(bg="white")

title_label = tk.Label(
    root,
    text="USER LOGIN",
    font=("Arial", 20, "bold"),
    bg="#ffffff",
    fg="blue"
)
title_label.pack(pady=5)

username_label = tk.Label(
    root,
    text="Username",
    font=("Arial", 11),
    bg="#ffffff",
    fg="black"
)
username_label.pack(pady=5)

username_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25
)
username_entry.pack(pady=5)

password_label = tk.Label(
    root,
    text="Password",
    font=("Arial", 12),
    bg="#ffffff",
    fg="black"
)
password_label.pack(pady=5)

password_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25,
    show="*"
)
password_entry.pack(pady=5)

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "pawii" and password == "#*#147":
        messagebox.showinfo(
            "LOGIN SUCCESSFULLY!",
            "Welcome Admin!"
        )
    else:
        messagebox.showerror(
            "LOGIN FAILED!",
            "Invalid Username and Password!"
        )

login_button = tk.Button(
    root,
    text="LOG IN",
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=20,
    command=login
)
login_button.pack(pady=20)

login_button.bind("<Enter>", lambda e: login_button.config(bg="#1d4ed8"))
login_button.bind("<Leave>", lambda e: login_button.config(bg="#2563eb"))
root.bind("<Return>", lambda e: login())

username_entry.focus()

root.mainloop()