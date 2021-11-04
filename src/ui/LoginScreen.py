#!/usr/bin/python
# Class for the login screen UI functions
import tkinter

def main_window():
    root_window = tkinter.Tk()
    root_window_label = tkinter.Label(root_window, text="Welcome to toy exchange")
    root_window_label.pack()
    root_window.mainloop()


class LoginScreen:
    pass