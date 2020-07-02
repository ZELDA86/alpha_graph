"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Project Name    : Alpha Graph
File Name       : frame.py
Encoding        : UTF-8
Creation Date   : June/28/2020

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


########## canvas area ##########
# root_graph = tk.Frame(root)
# root_graph.grid(column = 0, row = 0, padx =30, pady = 30)

root_graph = area(root, 0, 0, 30, 30)

canvas = FigureCanvasTkAgg(func.fig, master = root_graph)  # Generate canvas instance, Embedding fig in root
canvas.draw()
canvas.get_tk_widget().pack(ipadx = 0, ipady = 0)

########## function area ##########
root_func = tk.Frame(root)
root_func.grid(column = 1, row = 0, ipadx = 20)

label_x = tk.Label(root_func, text = "x-label", width = 12)
label_x.grid(column = 0, row = 0, pady = 5)
entry_x = tk.Entry(root_func, width = 37)
entry_x.grid(columnspan = 3, column = 1, row = 0, pady = 5)

label_y1 = tk.Label(root_func, text = "y1-label", width = 12)
label_y1.grid(column = 0, row = 1, pady = 5)
entry_y1 = tk.Entry(root_func, width = 37)
entry_y1.grid(columnspan = 3, column = 1, row = 1, pady = 5)

label_y2 = tk.Label(root_func, text = "y2-label", width = 12)
label_y2.grid(column = 0, row = 2, pady = 5)
entry_y2 = tk.Entry(root_func, width = 37)
entry_y2.grid(columnspan = 3, column = 1, row = 2, pady = 5)

label_space = tk.Label(root_func, text = "----------------------------------------------------------------------")
label_space.grid(columnspan = 4, row = 3)

label_xmin = tk.Label(root_func, text = "x-min", width = 12)
label_xmin.grid(column = 0, row = 4, pady = 5)
entry_xmin = tk.Entry(root_func, width = 12)
entry_xmin.grid(column = 1, row = 4, pady = 5, sticky = "w")
label_xmax = tk.Label(root_func, text = "x-max", width = 12)
label_xmax.grid(column = 2, row = 4, pady = 5)
entry_xmax = tk.Entry(root_func, width = 12)
entry_xmax.grid(column = 3, row = 4, pady = 5, sticky = "w")

label_y1min = tk.Label(root_func, text = "y1-min", width = 12)
label_y1min.grid(column = 0, row = 5, pady = 5)
entry_y1min = tk.Entry(root_func, width = 12)
entry_y1min.grid(column = 1, row = 5, pady = 5, sticky = "w")
label_y1max = tk.Label(root_func, text = "y1-max", width = 12)
label_y1max.grid(column = 2, row = 5, pady = 5)
entry_y1max = tk.Entry(root_func, width = 12)
entry_y1max.grid(column = 3, row = 5, pady = 5, sticky = "w")

label_y2min = tk.Label(root_func, text = "y2-min", width = 12)
label_y2min.grid(column = 0, row = 6, pady = 5)
entry_y2min = tk.Entry(root_func, width = 12)
entry_y2min.grid(column = 1, row = 6, pady = 5, sticky = "w")
label_y2max = tk.Label(root_func, text = "y2-max", width = 12)
label_y2max.grid(column = 2, row = 6, pady = 5)
entry_y2max = tk.Entry(root_func, width = 12)
entry_y2max.grid(column = 3, row = 6, pady = 5, sticky = "w")

label1 = tk.Label(root_func, text = "Marker Style")
label1.grid(column = 0, row = 7, pady = 5)
combo1 = ttk.Combobox(root_func, state = "readonly")
combo1["values"] = ("None", "Circle", "Square", "Diamond", "Triangle-up", "Triangle-down", "Triangle-left", "Triangle-right", "Cross")
combo1.current(1)
combo1.grid(columnspan = 3, column = 1, row = 7, pady = 5)

label2 = tk.Label(root_func, text = "Line Style")
label2.grid(column = 0, row = 8, pady = 5)
combo2 = ttk.Combobox(root_func, state = "readonly")
combo2["values"] = ("None", "Solid", "Dashed", "Dash Dot", "Dotted")
combo2.current(0)
combo2.grid(columnspan = 3, column = 1, row = 8, pady = 5)

label3 = tk.Label(root_func, text = "Color")
label3.grid(column = 0, row = 9, pady = 5)
combo3 = ttk.Combobox(root_func, state = "readonly")
combo3["values"] = ("Black", "Blue", "Red", "Green", "Yellow", "Cyan", "Magenta", "tab : blue", "tab : orange", "tab : green", "tab : red", "tab : purple", "tab : brown", "tab : pink", "tab : gray", "tab : olive", "tab : cyan")
combo3.current(0)
combo3.grid(columnspan = 3, column = 1, row = 9, pady = 5)

var = tk.IntVar(root, value = 22)

scale = tk.Scale(root_func, label = "Marker Size", orient = "horizontal", variable = var, from_ = 1, to = 30, length = 300)
scale.grid(columnspan = 4, row = 10, pady = 20)

ax1 = tk.Button(root_func, text = "Axis1", width = 7, command = lambda:[func.plt_ax1(), canvas.draw()])
ax1.grid(columnspan = 2, column = 0, row = 11)
ax2 = tk.Button(root_func, text = "Axis2", width = 7, command = lambda:[func.plt_ax2(), canvas.draw()])
ax2.grid(columnspan = 2, column = 2, row = 11)

button1 = tk.Button(root_func, text = "Save", width = 7, command = lambda:[func.text(0.4,0.3,"$x^2$",22), canvas.draw()])
button1.grid(columnspan = 4, row = 12, pady = 5, ipadx = 20)

button2 = tk.Button(root_func, text = "clear", width = 7, command = lambda:[func.plt.cla(), canvas.draw()])
button2.grid(columnspan = 4, row = 13, pady = 5, ipadx = 20)

button3 = tk.Button(root_func, text = "Exit", width = 7, command = lambda:root.destroy())
button3.grid(columnspan = 4, row = 14, pady = 5, ipadx = 20)

root.mainloop()