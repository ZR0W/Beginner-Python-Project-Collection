# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 22:03:05 2019

Based on tutorial@
https://likegeeks.com/python-gui-examples-tkinter-tutorial/#Add-a-combobox-widget

@author: Rowland Zhang
@contact: rowlandz@outlook.com
"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import Menu
from tkinter.ttk import Progressbar

window = tk.Tk()
# window setup
window.title("App")
window.geometry("700x400")
# label
l = tk.Label(window, text="Hello", font=("Arial Bold", 30))
l.grid(column=1, row=0)

def clicked():
    l.configure(text="You typed %s" % txtbox.get())
# button
btn = tk.Button(window, text="click!", command=clicked)
btn.configure(bg="sky blue", fg="azure")
btn.grid(column=0, row=0)
#text box
txtbox = tk.Entry(window, width=15)
txtbox.grid(column=0, row=1)
txtbox.focus()
#combo box
combo = ttk.Combobox(window)
combo["values"] = (1, 2, 3, "Text")
combo.current(0)
combo.grid(column=1, row=1)
# combo.get(), similar to txtbox.get()

# check button
checkbutton = tk.Checkbutton(window, text="check bos", var=True)
checkbutton.grid(column=2, row=0)
# radio button
selectedRadio = tk.IntVar()
radioBt1 = tk.Radiobutton(window, text="option", value=1, variable=selectedRadio)
radioBt2 = tk.Radiobutton(window, text="something else", value=2, variable=selectedRadio)
radioBt1.grid(column=2, row=1)
radioBt2.grid(column=3, row=1)
# button for radio button
def radioCheck():
    l.configure(text=selectedRadio.get())
    
btn_radio = tk.Button(window, text="get radio value", comman=radioCheck)
btn_radio.grid(column=4, row=1)
# scrolled text
"""is an option, I just didn't bother with it"""
#message box
def popup():
    messagebox.showinfo("Message", combo.get())
messageBt = tk.Button(window, text="message", command=popup)
messageBt.grid(column=2, row=2)
#spin box
spinvar = tk.IntVar()
spinvar.set(10)
spin = tk.Spinbox(window, from_=0, to=100, width=5, textvariable=spinvar)
spin.grid(column=3, row=2)
# progress bar
"""using ttk.style to customize the progress bar"""
barstyle = ttk.Style()
barstyle.theme_use("default")
barstyle.configure("black.Horizontal.TProgressvar", background="black")
bar = Progressbar(window, length=100, style="black.Horizontal.TProgressbar")
bar["value"] = 60
bar.grid(column=0, row=2)
# Menu
def menu_error():
    messagebox.showerror("Error from menu", "You clicked the Error tab from menu")
menu = Menu(window)
menuSub = Menu(menu, tearoff=0)
menuSub.add_command(label="Open")
menuSub.add_separator()
menuSub.add_command(label="New")
menuSub.add_command(label="Create")
menuSub.add_command(label="Error", command=menu_error)
menu.add_cascade(label="File", menu=menuSub)
menu.add_command(label="Exit")
window.config(menu=menu)
# tabs
"""
Example
perhaps? TODO
"""

"""
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control)
 
tab2 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text='First')
 
tab_control.add(tab2, text='Second')
 
lbl1 = Label(tab1, text= 'label1', padx=5, pady=5)
 
lbl1.grid(column=0, row=0)
 
lbl2 = Label(tab2, text= 'label2')
 
lbl2.grid(column=0, row=0)
 
tab_control.pack(expand=1, fill='both')
 
window.mainloop()
"""


window.mainloop()
