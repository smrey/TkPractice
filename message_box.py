import tkinter as tk
from tkinter import ttk
import logging


class MessageBox(tk.Tk):

    def __init__(self, box):
        tk.Tk.__init__(self, box)
        self.box = box
        self.grid()
        # Places popup in middle of screen
        #self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_toplevel()))
        self.mybutton = tk.Button(self, text="OK")
        self.mybutton.grid(column=0, row=2, sticky='EW')
        self.mybutton.bind("<ButtonRelease-1>", self.button_callback)
        self.popup_text = tk.Text(self, state="disabled")
        self.popup_text.grid(column=0, row=1)

    def button_callback(self, event):
        self.destroy()


class MyEntryWindow:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.label = ttk.Label(text="Do something!")
        self.label.grid(column=0, row=0)
        self.e = ttk.Entry()
        self.e.grid(column=1, row=0, pady=10)
        self.entry_button = tk.Button(self, text="Entered stuff")
        self.entry_button.grid(column=2, row=0)
        self.entry_button.bind("<ButtonRelease-1>", self.entry_button_callback)

    def entry_button_callback(self, event):
        return self.e


class MyHandlerText(logging.StreamHandler):
    def __init__(self, textctrl):
        logging.StreamHandler.__init__(self) # initialize parent
        self.textctrl = textctrl

    def emit(self, record):
        msg = self.format(record)
        self.textctrl.config(state="normal")
        self.textctrl.insert("end", msg + "\n")
        self.flush()
        self.textctrl.config(state="disabled")
