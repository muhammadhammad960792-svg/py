from tkinter import*
from tkinter import messagebox 
from PIL import Image,ImageTk
window=Tk()
window.geometry("400x400")
title=Label(window,text="My Photo Album",fg="White",bg="purple",width=40)
title.pack(pady=10)
img_file=Image.open("13.png")
img_file=img_file.resize((300,180))
photo=ImageTk.PhotoImage(img_file)
pic=Label(window,image=photo)
pic.pack(pady=5)
def show_message():
    messagebox.showinfo("Great!","You clicked the photo!")
msg_btn=Button(window,text='Click to react',bg="blue",fg="white",command=show_message)
msg_btn.pack(pady=10)


window.mainloop()