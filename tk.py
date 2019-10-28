#from tkinter import *
import tkinter as tk

class MyDialog:

    def __init__(self, parent):

        top = self.top = tk.Toplevel(parent)

        tk.Label(top, text="Value").pack()

        self.e = tk.Entry(top)
        self.e.pack(padx=5)

        b = tk.Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):

        print("value is", self.e.get())

        self.top.destroy()


root = tk.Tk()
tk.Button(root, text="Hello!").pack()
root.update()

d = MyDialog(root)

root.wait_window(d.top)