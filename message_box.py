import tkinter as tk
from tkinter import ttk
import logging


class Dialog(tk.Toplevel):

    def __init__(self, parent, title=None):
        tk.Toplevel.__init__(self, parent)
        self.transient(parent)
        if title:
            self.title(title)
        self.parent = parent
        self.result = None
        body = tk.Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)
        self.buttonbox()
        self.grab_set()
        if not self.initial_focus:
            self.initial_focus = self
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("+%d+%d" % (parent.winfo_rootx() + 50,
                                    parent.winfo_rooty() + 50))
        self.initial_focus.focus_set()
        self.wait_window(self)

    # construction hooks
    def body(self, master):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden
        pass

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons
        box = tk.Frame(self)
        w = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()

    # standard button semantics
    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set()  # put focus back
            return
        self.withdraw()
        self.update_idletasks()
        self.apply()
        self.cancel()

    def cancel(self, event=None):
        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    # command hooks
    def validate(self):
        return 1  # override

    def apply(self):
        pass  # override


class MyEntryWindow(Dialog):
    def body(self, master):
        self.grid()
        self.wm_title("CRUK Generator Data Entry")
        master.grid()
        self.label1 = ttk.Label(master, text="Enter sample identifier")
        self.label1.grid(column=0, row=0)
        self.e1 = ttk.Entry(master)
        self.e1.grid(column=1, row=0, pady=10)
        self.label2 = ttk.Label(master, text="Enter worksheet identifier if applicable")
        self.label2.grid(column=0, row=1)
        self.e2 = ttk.Entry(master)
        self.e2.grid(column=1, row=1, pady=10)
        self.label3 = ttk.Label(master, text="Enter authoriser's initials")
        self.label3.grid(column=0, row=2)
        self.e3 = ttk.Entry(master)
        self.e3.grid(column=1, row=2, pady=10)
        self.label4 = ttk.Label(master, text="Enter sample status (options are s (sequenced), f (failed) or "
                                             "withdrawn))")
        self.label4.grid(column=0, row=3)
        self.e4 = ttk.Entry(master)
        self.e4.grid(column=1, row=3, pady=10)
        return self.e1 # Intial focus will be here

    def apply(self):
        sample = self.e1.get()
        worksheet = self.e2.get()
        authoriser = self.e3.get()
        status = self.e4.get()
        print(sample, worksheet, authoriser, status)

    def entry_button_callback(self, event):
        self.destroy()


class MessageBox:

    def __init__(self, box):
        self.top = tk.Toplevel(box)
        self.top.grid()
        self.top.wm_title("CRUK Generator")
        self.mybutton = tk.Button(self.top, text="OK")
        self.mybutton.grid(column=0, row=2, sticky='EW')
        self.mybutton.bind("<ButtonRelease-1>", self.button_callback)
        self.popup_text = tk.Text(self.top, state="disabled")
        self.popup_text.grid(column=0, row=1)

    def button_callback(self, event):
        self.top.destroy()

'''
class MessageBox(Dialog):

    def body(self, master):
        self.grid()
        self.wm_title("CRUK Generator Log")
        self.mybutton = tk.Button(master, text="OK")
        self.mybutton.grid(column=0, row=2, sticky='EW')
        self.mybutton.bind("<ButtonRelease-1>", self.button_callback)
        self.popup_text = tk.Text(master, state="disabled")
        self.popup_text.grid(column=0, row=1)

    def buttonbox(self):
        pass

    def button_callback(self, event):
        self.destroy()
'''

class MyHandlerText(logging.StreamHandler):
    def __init__(self, textctrl):
        logging.StreamHandler.__init__(self)  # initialize parent
        self.textctrl = textctrl

    def emit(self, record):
        msg = self.format(record)
        self.textctrl.config(state="normal")
        self.textctrl.insert("end", msg + "\n")
        self.flush()
        self.textctrl.config(state="disabled")

def main():
    print("Cannot be run")

if __name__ == '__main__':
    main()