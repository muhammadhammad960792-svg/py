from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to calculate the denmination count?")
    if MsgBox == 'ok':
        topwin()

button1 = Button(root, text="Lets get started!", command=msg, bg='brown', fg='white')
button1.place(x=260, y=360)
def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg='light blue')
    top.geometry('600x350+50+50')
    label=Label(top, text="Enter total amount", bg='light grey')
    entry =Entry(top)
    lbl = Label(top, text="hereare number of notes for each denomination",bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    t1 =Entry(top)
    t2 =Entry(top)
    t3 =Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount%= 500
            note100 = amount // 100
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(0, str(note2000))
            t2.insert(0, str(note500))
            t3.insert(0, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

        btn = Button 