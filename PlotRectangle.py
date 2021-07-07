# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 09:31:25 2021

@author: cmartinez
"""

from tkinter import *

root = Tk()
canvas = Canvas(root, width=550, height=550)
canvas.pack()
canvas.create_rectangle(50, 50, 500, 500, fill="red")
canvas.create_line(20, 250, 530, 250, fill="black")
canvas.create_oval(60, 60, 490, 490)
root.mainloop()
