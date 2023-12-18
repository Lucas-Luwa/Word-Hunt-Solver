import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plotter(inputLines, filledTile=None, initChars=None):
    gridNum = 4

    fig = Figure(figsize=(6, 6))
    plot = fig.add_subplot(1, 1, 1)

    for line in inputLines:
        start = line[0]; end = line[1]
        plot.plot([start % gridNum, end % gridNum], [start // gridNum, end // gridNum], 'k-')

    counter = 0
    for x in range(gridNum):
        for y in range(gridNum):
            plot.annotate(initChars[counter], (y, x), color='black', fontsize=36,
                          ha='center', va='center')
            counter+=1
    
    if filledTile is not None:
        fillSqX = filledTile % gridNum -0.5
        fillSqY = filledTile // gridNum - 0.5
        plot.fill_between([fillSqX, fillSqX + 1], [fillSqY, fillSqY], [fillSqY + 1, fillSqY + 1], color='lightgreen', alpha=0.75)

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
    plotter(allWords[currLineNum], initNode[currLineNum], initChars)
    currWord.set(f"Current Word: {wordValues[currLineNum]} | Word #: {currLineNum + 1}/{numElements} | Points: {pointValues[currLineNum]}")


def prevWord(event):
    global currLineNum
    currLineNum = (currLineNum - 1) % len(allWords)
    plotter(allWords[currLineNum], initNode[currLineNum], initChars)
    currWord.set(f"Current Word: {wordValues[currLineNum]} | Word #: {currLineNum + 1}/{numElements} | Points: {pointValues[currLineNum]}")


def mainContents(gridStart, gridContents):
    global window, currLineNum, allWords, wordValues, currWord, initNode, numElements, pointValues, initChars
    if len(gridContents) == 0: 
        print("Error: No valid words")
        return 
    initChars = gridStart
    window = tk.Tk()
    window.title("Solved Words")

    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)

    allWords = []
    wordValues = []
    initNode = []
    pointValues = []
    for element in gridContents:
        # print(element[0], element[1])
        wordValues.append(element[0])
        currInitNode, edgeList = edgeGenerator(element[1])
        allWords.append(edgeList)
        initNode.append(currInitNode)
        pointValues.append(pointCalc(len(element[0])))

    numElements = len(wordValues)
    print("Potential Total: ", sum(pointValues))

    currLineNum = 0
    currWord = tk.StringVar()
    currWord.set(f"Current Word: {wordValues[currLineNum]} | Word #: {currLineNum + 1}/{numElements} | Points: {pointValues[currLineNum]}")

    wordLabel = tk.Label(window, textvariable=currWord, font=("Arial", 12))
    wordLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    plotter(allWords[currLineNum], initNode[0], initChars)

    window.bind("<Right>", nxtWord)
    window.bind("<Left>", prevWord)

    window.mainloop()

def edgeGenerator(inputStr):
    retList = []
    currX = int(inputStr[0])
    currY = int(inputStr[1])
    currNode = (currX * 4 + currY)
    initNode = currNode
    index = 2
    while index < len(inputStr):
        nextX = int(inputStr[index])
        nextY = int(inputStr[index + 1])
        nextNode = (nextX * 4 + nextY)
        retList.append((currNode, nextNode))
        currNode = nextNode
        index+=2
    return initNode, retList

def pointCalc(num):
    vals = [100, 400, 800, 1200,1800, 2200]
    return vals[num - 3]

# Initial Testing
# mainContents("abcdefghijklmnop", [('hedge', '2111102030'), ('badge', '0100102011'), ('badge', '0100102030'), ('bead', '01110010'), ('head', '21110010'), 
#               ('bade', '01001011'), ('edge', '11102030'), ('ghee', '20213223'), ('abed', '00011110'), ('dae', '100011'), ('edh', '111021'), 
#               ('gee', '132332'), ('ged', '201110'), ('beg', '011120'), ('fee', '313223'), ('deg', '101120'), ('fee', '332332'), 
#               ('bad', '010010'), ('jed', '221110'), ('fee', '122332'), ('fee', '333223'), ('ade', '001011'), ('fed', '121110'), 
#               ('bae', '010011'), ('deb', '101101'), ('bed', '011110'), ('dab', '100001')])
