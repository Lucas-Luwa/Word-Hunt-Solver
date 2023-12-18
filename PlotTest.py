import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plotter():
    gridNum = 4

    lines = [(0, 5), (1, 2), (2, 3), (4, 4), (1, 5), (5, 6), (3, 7)]
    plt.figure(figsize=(6, 6))

    for line in lines:
        start = line[0]; end = line[1]
        plt.plot([start % gridNum, end % gridNum], [start // gridNum, end // gridNum], 'k-')
    plt.grid(True)
    plt.xticks(np.arange(-0.5, gridNum), [])
    plt.yticks(np.arange(-0.5, gridNum), [])
    plt.gca().invert_yaxis()
    plt.show()

plotter()