from tkinter import *


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_gui()

    def init_gui(self):
        self.parent.title("age checker | v1.1")
        self.config(bg="#373634")
        self.pack(fill=BOTH, expand=1)
        canvas1 = Canvas(self, relief=FLAT, bg="#6B6A65", width=220, height=500)
        canvas1.pack(side=TOP, anchor=NW, padx=10, pady=50)
        button1 = Button(canvas1, text="Quit", command=self.quit, anchor=W)
        button1.configure(width=10, activebackground="grey", relief=FLAT)
        button1.place(x=10, y=10)
        user = make_entry(10, 50, canvas1, "User name", 10)
        age = make_entry(10, 90, canvas1, "age", 10)


def make_entry(x, y, parent, caption, width=None, **options):
    canvas_border = Canvas(parent, bg="white", width=180, height=25)
    canvas_border.place(x=x, y=y)
    Label(canvas_border, text=caption).place(x=5, y=5)
    enter1 = Entry(canvas_border)
    enter1.configure(width=width)
    enter1.place(x=(5+70), y=5)
    if width:
        enter1.config(width=width)
    return enter1


def main():
    root = Tk()
    root.geometry('800x600+10+50')
    app = Example(root)
    app.mainloop()


if __name__ == '__main__':
    main()
