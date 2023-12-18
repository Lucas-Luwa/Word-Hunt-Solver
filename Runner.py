import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plotter(lines_to_draw):
    gridNum = 4

    fig = Figure(figsize=(6, 6))
    plot = fig.add_subplot(1, 1, 1)

    for line in lines_to_draw:
        start = line[0]; end = line[1]
        plot.plot([start % gridNum, end % gridNum], [start // gridNum, end // gridNum], 'k-')

    plot.grid(True)
    plot.set_xticks(np.arange(-0.5, gridNum))
    plot.set_yticks(np.arange(-0.5, gridNum))
    plot.invert_yaxis()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

def nxtWord(event):
    global currLineNum
    currLineNum = (currLineNum + 1) % len(allWords)
    plotter(allWords[currLineNum])

def prevWord(event):
    global currLineNum
    currLineNum = (currLineNum - 1) % len(allWords)
    plotter(allWords[currLineNum])

window = tk.Tk()
window.title("Solved Words")

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

allWords = [
    [(0, 1), (1, 2), (2, 3), (0, 4), (1,
                                       5), (5, 6), (3, 7)],
    [(0, 1), (1, 2), (2, 3), (3, 0), (0, 5), (1, 6), (2, 7), (3, 4)]
    # Add more sets of lines as needed
]

currLineNum = 0

plotter(allWords[currLineNum])

window.bind("<Right>", nxtWord)
window.bind("<Left>", prevWord)

window.mainloop()
