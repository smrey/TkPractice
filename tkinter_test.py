import logging
import os
import sys
import time
import tkinter as tk


class Tester:

    def __init__(self):
        self.root = tk.Tk()
        self.root.grid()
        self.root.but = tk.Button(self.root, text='mee')
        self.root.but.grid(column=0, row=2, sticky='EW')
        self.root.update()

        # Initialise an instance of the module logger
        self.ml = ModuleLogger(self.root)
        self.log = self.ml.module_logger
        self.popup = self.ml.my_message


    def handle_exception(self, exc_type, exc_value, exc_traceback):
        # Debug is used as this type of error cannot be attempted to be passed to the popup as will happen with
        # use of critical or error level
        self.log.debug("An exception occurred", exc_info=(exc_type, exc_value, exc_traceback))
        # Pass write-out of error to popup
        self.log.critical(f"[CRITICAL ERROR]: {exc_value}. See bioinformatics team for support [CRITICAL ERROR]")
        self.log.critical("\n")
        self.log.critical("****[ERROR] PDF AND XML FILE HAVE NOT BEEN CORRECTLY GENERATED [ERROR]****")
        self.root.mainloop()

    def test_stuff(self):
        print("starting")
        time.sleep(1)
        self.log.info("hiya")
        time.sleep(2)
        #raise Exception("Huge problemo")
        self.root.mainloop()

class ModuleLogger:

    def __init__(self, parent_window):
        # Create pop-up box for entering data
        # TODO Placed weirdly for testing
        from message_box import MyEntryWindow
        entering_data = MyEntryWindow(parent_window)

        # Create log file pop-up box
        from message_box import MessageBox, MyHandlerText
        self.my_message = MessageBox(parent_window)
        #self.my_message.wm_title("CRUK Generator")
        self.module_logger = logging.getLogger(__name__)
        self.module_logger.setLevel(logging.DEBUG)

        # Create handler to route messages to popup
        gui_handler = MyHandlerText(self.my_message.popup_text)
        gui_handler.setLevel(logging.INFO)
        self.module_logger.addHandler(gui_handler)

        # Create handler to route debug messages to file
        #stdout_handler = logging.StreamHandler(sys.stdout)
        #stdout_handler.setLevel(logging.DEBUG)
        #self.module_logger.addHandler(stdout_handler)

        # Create handler to route messages to file
        file_handler = logging.FileHandler(os.path.join(os.getcwd(), "log.log"))
        file_handler.setLevel(logging.DEBUG)
        self.module_logger.addHandler(file_handler)



def main():
    t = Tester()
    sys.excepthook = t.handle_exception
    t.test_stuff()


if __name__ == '__main__':
    main()