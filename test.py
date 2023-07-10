import tkinter as tk
import re

# Regular expression patterns for different password formats
password_patterns = {
    "weak": r"^[a-zA-Z]{8,}$",
    "strong": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",
    "diamond": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=])[a-zA-Z\d@#$%^&+=]{8,}$"
}

def check_password_level(password):
    for level, pattern in password_patterns.items():
        if re.match(pattern, password):
            return level
    return "Unknown"

def update_status():
    password = password_entry.get()
    level = check_password_level(password)
    status_label.config(text=f"Status: {level}")

root = tk.Tk()
root.title("Password Status")

password_label = tk.Label(root, text="Enter your password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

status_label = tk.Label(root, text="Status:")
status_label.pack()

password_entry.bind("<KeyRelease>", lambda event: update_status())

root.mainloop()
