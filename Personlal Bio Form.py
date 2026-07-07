# Step 1: Import Tkinter
import tkinter as tk
from tkinter import messagebox

# Step 2: Create the main window
root = tk.Tk()
root.title("Personal Bio Form")
root.geometry("500x450")

# Step 3: Add a frame
frame = tk.Frame(root, padx=20, pady=20)
frame.grid(row=0, column=0)

# Step 6: Create the button function
def submit_data():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    email = email_entry.get()
    bio = bio_text.get("1.0", tk.END).strip()

    message = (
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Gender: {gender}\n"
        f"Email: {email}\n"
        f"Bio: {bio}"
    )

    messagebox.showinfo("Personal Bio", message)

# Step 4: Add label widgets
title_label = tk.Label(frame, text="Personal Bio Form",
                       font=("Arial", 16, "bold"))

name_label = tk.Label(frame, text="Name:")
age_label = tk.Label(frame, text="Age:")
gender_label = tk.Label(frame, text="Gender:")
email_label = tk.Label(frame, text="Email:")
bio_label = tk.Label(frame, text="Bio:")

# Step 5: Add Entry and Text widgets
name_entry = tk.Entry(frame, width=30)
age_entry = tk.Entry(frame, width=30)
gender_entry = tk.Entry(frame, width=30)
email_entry = tk.Entry(frame, width=30)

bio_text = tk.Text(frame, width=30, height=5)

submit_button = tk.Button(frame, text="Submit", command=submit_data)

# Step 7: Arrange everything with Grid
title_label.grid(row=0, column=0, columnspan=2, pady=10)

name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
name_entry.grid(row=1, column=1, padx=10, pady=5)

age_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
age_entry.grid(row=2, column=1, padx=10, pady=5)

gender_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
gender_entry.grid(row=3, column=1, padx=10, pady=5)

email_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
email_entry.grid(row=4, column=1, padx=10, pady=5)

bio_label.grid(row=5, column=0, padx=10, pady=5, sticky="nw")
bio_text.grid(row=5, column=1, padx=10, pady=5)

submit_button.grid(row=6, column=0, columnspan=2, pady=15)

# Step 9: Run the window
root.mainloop()