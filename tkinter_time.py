import tkinter as tk
from tkinter import *
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.time_label = Label(self.master, font=("Arial", 24), bg="white", fg="black")
        self.time_label.pack(padx=20, pady=20)
        
        self.update_time()
    
    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        
        # Schedule the next update after 1 second (1000 milliseconds)
        self.master.after(1000, self.update_time)

root = Tk()
app = Application(root)
app.mainloop()

