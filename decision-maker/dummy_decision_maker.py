# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 01:31:46 2019

Project: (Crappy) Decision Maker
@author: Rowland Zhang
@contact: rowlandz@outlook.com
"""

import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import Menu
from tkinter.ttk import Progressbar
import random

"""global variables"""
window = tk.Tk()
window_width = 700
window_height = 400

"""function declaration"""

def window_setup():
    window.title("App")
    window.option_add('*font', ('verdana', 12, 'bold'))
    window.configure(bg="Honeydew")
    window.geometry(str(window_width) + "x" + str(window_height))
    
def make_label(c, r):
    l = tk.Label(window, text="Test", font=("Arial Bold", 30))
    l.grid(column=c, row=r)

def make_menu():
    menu = Menu(window)
    menuSub = Menu(menu, tearoff=0)
    menuSub.add_command(label="Open")
    menuSub.add_separator()
    menuSub.add_command(label="New")
    menuSub.add_command(label="Create")
    menuSub.add_command(label="Error", command=popup)
    menu.add_cascade(label="File", menu=menuSub)
    menu.add_command(label="Exit")
    window.config(menu=menu)

def popup():
    messagebox.showerror("Error from menu", "You clicked the Error tab from menu")

def make_ui():
    """
    General layout:
        9x9 grid
        [combobox] | [Entry] | [label]
        [] | [button] | []
        [] | [Entry] | []
    """
    #combo box
    combo = ttk.Combobox(window)
    combo["values"] = ("Should", "Can", "Would", "Will")
    combo.current(0)
    #combo.grid(column=0, row=0)
    combo.pack()
    # combo.get(), similar to txtbox.get()
    #text box
    txtbox = tk.Entry(window, width=30)
    #txtbox.grid(column=1, row=0)
    txtbox.pack()
    txtbox.focus()
    # label
    label = tk.Label(window, text="?", font=("Arial Bold", 20))
    #label.grid(column=2, row=0)
    label.pack()
    
    def respond():
        num = random.randint(0, 1)
        if num == 0:
            output = "Yes"
        if num == 1:
            output = "No"
        response_label.configure(text="I think the answer is %s" % output)
    
    # button
    btn = tk.Button(window, text="Answer", command=respond)
    btn.configure(bg="sky blue", fg="azure")
    #btn.grid(column=1, row=1)
    btn.pack()
    # response label
    response_label = tk.Label(window, text="", font=("Arial Bold", 20))
    #response_label.grid(column=1, row=2)
    response_label.pack()

def main():
    window_setup()
    make_menu()
    make_ui()
    window.mainloop()
    
main()