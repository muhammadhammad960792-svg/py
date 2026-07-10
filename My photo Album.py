import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Create the Main Tkinter Window
root = tk.Tk()
root.title("My Photo Album")
root.geometry("600x500")
root.configure(bg="white")

# Add a Title Label
title = tk.Label(
    root,
    text="My Photo Album",
    font=("Arial", 20, "bold"),
    bg="white",
    fg="blue"
)
title.pack(pady=10)

# Add an Image Using PIL
image = Image.open("photo.jpg")      # Replace with your image file
image = image.resize((350, 250))

photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo, bg="white")
image_label.pack(pady=10)

# Create a Message Box Function
def show_message():
    messagebox.showinfo("Photo Album", "Welcome to My Photo Album!")

# Create a Top-Level Function
def open_window():
    top = tk.Toplevel(root)
    top.title("About")
    top.geometry("300x150")

    label = tk.Label(
        top,
        text="This is My Photo Album.\nCreated using Python Tkinter.",
        font=("Arial", 14)
    )
    label.pack(pady=30)

# Add Buttons
message_btn = tk.Button(root, text="Show Message", command=show_message)
message_btn.pack(pady=5)

about_btn = tk.Button(root, text="About", command=open_window)
about_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(pady=5)

# Run the Application
root.mainloop()