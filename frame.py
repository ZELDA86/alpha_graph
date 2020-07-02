"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Project Name    : Alpha Graph
File Name       : frame.py
Encoding        : UTF-8
Creation Date   : July/2/2020

Copyright (c) 2020 Hiroki MATSUI. All rights reserved.

This source code or any portion thereof must not be  
reproduced or used in any manner whatsoever.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import tkinter as tk
import tkinter.ttk as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import func

root = tk.Tk()
root.title("alpha Graph")

def area(base, col, row, padx = 0, pady = 0, ipadx = 0, ipady = 0):
    area = tk.Frame(base)
    area.grid(column = col, row = row, padx = padx, pady = pady, ipadx = ipadx, ipady = ipady)
    return area

def entry(base, txt, row, col = 0, lw = 15, ew = 15, colspan_l = 1, colspan_e = 1):
    label = tk.Label(base, text = txt, width = lw)
    label.grid(columnspan = colspan_l, column = col, row = row, pady = 3)
    entry = tk.Entry(base, width = ew)
    entry.grid(columnspan = colspan_e, column = col + 1, row = row, pady = 3, sticky = tk.W)
    return label, entry

def button(base, txt, row, col = 0, width = 7, columnspan = 1, cmd = None):
    button = tk.Button(base, text = txt, width = width, command = cmd)
    button.grid(columnspan = columnspan, row = row, column = col, pady = 3, ipadx = 3)
    return button

def spin_scale(base, txt, row, col = 0, f = 1, t = 30, inc = 1, length = 150, pady = 5, columnspan = 4, value = 22):
    var = tk.StringVar(root, value = value)
    label = tk.Label(base, text = txt, width = 12)
    label.grid(row = row, column = col)
    spinbox = tk.Spinbox(base, textvariable = var, from_ = f, to = t, increment = inc, width = 5)
    spinbox.grid(row = row, column = col + 1, sticky = tk.W)
    scale = tk.Scale(base, label = None, orient = "horizontal", variable = var, from_ = f, to = t, length = length, resolution = inc)
    scale.grid(columnspan = columnspan, row = row, column = col + 2, pady = pady, sticky = tk.W)
    return label,spinbox,scale

marker = ("None", "Circle", "Square", "Diamond", "Triangle-up", "Triangle-down", "Triangle-left", "Triangle-right", "Cross")
line = ("None", "Solid", "Dashed", "Dash Dot", "Dotted")
color = ("Black", "Blue", "Red", "Green", "Yellow", "Cyan", "Magenta", "tab : blue", "tab : orange", "tab : green", "tab : red", "tab : purple", "tab : brown", "tab : pink", "tab : gray", "tab : olive", "tab : cyan")

########## canvas area ##########
root_graph = area(root, 0, 0, padx = 30, pady = 30)

canvas = FigureCanvasTkAgg(func.fig, master = root_graph)  # Generate canvas instance, Embedding fig in root
canvas.draw()
canvas.get_tk_widget().pack(ipadx = 0, ipady = 0)

########## function area ##########
root_func = area(root, 1, 0, ipadx = 20)

label_x = entry(root_func, "x_label", row = 0, ew = 37, colspan_e = 3)
label_y1 = entry(root_func, "y1-label", row = 1, ew = 37, colspan_e = 3)
label_y2 = entry(root_func, "y2-label", row = 2, ew = 37, colspan_e = 3)

label_xmin = entry(root_func, "x-min", row = 3, lw = 12, ew = 12)
label_xmax = entry(root_func, "x-max", row = 3, col = 2, lw = 12, ew = 12)

label_y1min = entry(root_func, "y1-min", row = 4, lw = 12, ew = 12)
label_y1max = entry(root_func, "y1-max", row = 4, col = 2, lw = 12, ew = 12)

label_xmin = entry(root_func, "y2-min", row = 5, lw = 12, ew = 12)
label_xmax = entry(root_func, "y2-max", row = 5, col = 2, lw = 12, ew = 12)

legend = entry(root_func, "Legend", row = 6, lw = 12, ew = 37, colspan_e = 3)

label1 = tk.Label(root_func, text = "Marker Style")
label1.grid(column = 0, row = 7, pady = 5)
combo1 = ttk.Combobox(root_func, state = "readonly")
combo1["values"] = ("None", "Circle", "Square", "Diamond", "Triangle-up", "Triangle-down", "Triangle-left", "Triangle-right", "Cross")
combo1.current(1)
combo1.grid(columnspan = 3, column = 1, row = 7, pady = 5, sticky = tk.W)

label2 = tk.Label(root_func, text = "Line Style")
label2.grid(column = 0, row = 8, pady = 5)
combo2 = ttk.Combobox(root_func, state = "readonly")
combo2["values"] = ("None", "Solid", "Dashed", "Dash Dot", "Dotted")
combo2.current(0)
combo2.grid(columnspan = 3, column = 1, row = 8, pady = 5, sticky = tk.W)

label3 = tk.Label(root_func, text = "Color")
label3.grid(column = 0, row = 9, pady = 5)
combo3 = ttk.Combobox(root_func, state = "readonly")
combo3["values"] = ("Black", "Blue", "Red", "Green", "Yellow", "Cyan", "Magenta", "tab : blue", "tab : orange", "tab : green", "tab : red", "tab : purple", "tab : brown", "tab : pink", "tab : gray", "tab : olive", "tab : cyan")
combo3.current(0)
combo3.grid(columnspan = 3, column = 1, row = 9, pady = 5, sticky = tk.W)

scale_marker = spin_scale(root_func, "Marker size", row = 10, length = 220, columnspan = 2, f = 1, t = 5, value = 1, inc = 0.1)
scale_line = spin_scale(root_func, "Line width", row = 11, length = 220, columnspan = 2, f = 1, t = 5, value = 1, inc = 0.1)
scale_text = spin_scale(root_func, "Text size", row = 12, length = 220, columnspan = 2, f = 1, t = 30, value = 22, inc = 1)

button_ax1 = button(root_func, "Axis1", row = 14, col = 0)
button_ax2 = button(root_func, "Axis2", row = 14, col = 1)
button_clear = button(root_func, "Clear", row = 14, col = 3)
entry_save = entry(root_func, "file-name", row = 15, ew = 24, colspan_e = 2)
button_save = button(root_func, "Save", row = 15, col = 3)
button_exit = button(root_func, "Exit", row = 16, columnspan = 4, cmd = lambda:root.destroy())

root.mainloop()