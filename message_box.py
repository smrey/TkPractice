import tkinter as tk
from tkinter import ttk
import logging


class MessageBox(): # Putting tk.Tk here makes an additional popup generic tk box

    def __init__(self, box):
        #tk.Tk.__init__(self, None)
        #self.box = box
        self.top = tk.Toplevel(box) # This is making a popup for some reason- it isn't root it is another new tk object
        self.top.grid()
        # Places popup in middle of screen
        #self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_toplevel()))
        self.top.wm_title("CRUK Generator")
        self.mybutton = tk.Button(self.top, text="OK")
        self.mybutton.grid(column=0, row=2, sticky='EW')
        self.mybutton.bind("<ButtonRelease-1>", self.button_callback)
        self.popup_text = tk.Text(self.top, state="disabled")
        self.popup_text.grid(column=0, row=1)

        #self.tk = tk

    def button_callback(self, event):
        self.top.destroy()


class MyEntryWindow(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, None)
        self.top = tk.Toplevel(parent)  # This is making a popup for some reason- it isn't parent it is another new tk object
        self.top.grid()
        self.top.grab_set()
        self.label = ttk.Label(self.top, text="Do something!")
        self.label.grid(column=0, row=0)
        self.e = ttk.Entry(self.top)
        self.e.grid(column=1, row=0, pady=10)
        self.entry_button = ttk.Button(self.top, text="Entered stuff")
        self.entry_button.grid(column=2, row=0)
        self.entry_button.bind("<ButtonRelease-1>", self.entry_button_callback)
        #self.destroy()

    def entry_button_callback(self, event):
        self.top.destroy()
        return self.e


class MyHandlerText(logging.StreamHandler):
    def __init__(self, textctrl):
        logging.StreamHandler.__init__(self)  # initialize parent
        self.textctrl = textctrl

    def emit(self, record):
        msg = self.format(record)
        self.textctrl.config(state="normal")
        self.textctrl.insert("end", msg + "\n")
        #self.flush()
        #self.textctrl.config(state="disabled")

def main():
    print("Cannot be run")

if __name__ == '__main__':
    main()