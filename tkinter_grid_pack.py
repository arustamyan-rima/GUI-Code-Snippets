"""
GEOMETRY MANAGER PACK
"""

from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        apple = Label(master, text = "apple", bg = "green", fg = "white", font = "bold")
        watermelon = Label(master, text = "watermelon", bg = "pink", fg = "black", font = "italic")
        cherry = Label(master, text = "cherry", bg = "red", fg = "black", font = "underline")
        apple.pack(fill = X, padx = 20, pady = 20),
        watermelon.pack(fill = X, padx = 20, pady = 20),
        cherry.pack(fill = X, padx = 20, pady = 20)

root = Tk()
app = Application(root)
app.mainloop()

"""
GEOMETRY MANAGER GRID
"""

class Application_2(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        rainbow1 = Label(master, text = "red", bg = "red", fg = "white", font = "bold")
        rainbow2 = Label(master, text = "orange", bg = "orange", fg = "black", font = "italic")
        rainbow3 = Label(master, text = "yellow", bg = "yellow", fg = "black", font = "underline")
        rainbow4 = Label(master, text = "green", bg = "green", fg = "black", font = "bold")
        rainbow5 = Label(master, text = "blue", bg = "blue", fg = "black", font = "italic")
        rainbow6 = Label(master, text = "indigo", bg = "indigo", fg = "black", font = "underline")
        rainbow7 = Label(master, text = "violet", bg = "violet", fg = "black", font = "bold")

        rainbow1.grid(row = 0, column = 0, padx = 10, pady = 10, ipadx = 30, ipady = 20)
        rainbow2.grid(row = 1, column = 0, padx = 10, pady = 10, ipadx = 30, ipady = 20)
        rainbow3.grid(row = 2, column = 0, padx = 10, pady = 10, ipadx = 30, ipady = 20)
        rainbow4.grid(row = 3, column = 0, padx = 10, pady = 10, ipadx = 30, ipady = 20)
        rainbow5.grid(row = 4, column = 0, padx = 10, pady = 10, ipadx = 30, ipady = 20)
        rainbow6.grid(row = 5, column = 0, padx = 10, pady = 10, ipadx = 30, ipady = 20)
        rainbow7.grid(row = 6, column = 0, padx = 10, pady = 10, ipadx = 30, ipady = 20)

root = Tk()
app = Application_2(root)
app.mainloop()