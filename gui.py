from tkinter import *

root = Tk()

w = Canvas(root, width=600, height=400, bg='#373634')
w.pack()

w.create_rectangle(0, 0, 600, 30, fill="#6B6A65", outline="grey")


def make_entry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry


user = make_entry(w, "User name:", 10)
password = make_entry(w, "Password", 10, show="*")
var = StringVar(root)
var.set("January")
option = OptionMenu(root, var, "January", "February", "March", "April", "May", "June", "July")
option.pack()


def ok():
    print("value is: ", var.get())
    root.quit()


button = Button(w, text="OK", command=ok)
button.pack()

mainloop()
