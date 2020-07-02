"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Project Name    : Alpha Graph
File Name       : func.py
Encoding        : UTF-8
Creation Date   : July/2/2020

Copyright (c) 2020 Hiroki MATSUI. All rights reserved.

This source code or any portion thereof must not be  
reproduced or used in any manner whatsoever.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] ='Times New Roman'
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams['xtick.major.width'] = 1
plt.rcParams['ytick.major.width'] = 1
plt.rcParams['font.size'] = 22
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams["legend.markerscale"] = 1.5
plt.rcParams["legend.fancybox"] = False
plt.rcParams["legend.framealpha"] = None
plt.rcParams["legend.edgecolor"] = 'black'

fig, ax1 = plt.subplots(figsize = (7,7))

def plt_ax1():
    x1 = np.linspace(0,10,100)
    y1 = 5 * np.cos(x1)
    ax1.plot(x1, y1, marker = "o", markersize = 7, linestyle = "", clip_on = False, color = "tab:olive")

def plt_ax2():
    x2 = np.linspace(0,10)
    y2 = np.sin(x2)
    ax2 = ax1.twinx()
    ax2.plot(x2, y2, marker = "s", markersize = 5, linestyle = "", clip_on = False, color = "tab:orange")

def text(x, y, txt, fontsize):
    plt.text(x, y, txt, fontsize = fontsize)