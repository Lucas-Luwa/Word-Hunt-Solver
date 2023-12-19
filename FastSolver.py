import tkinter as tk
import nltk
import time
import Visualizer


# Add this back for first time users
# nltk.download('words')
englWords = set(nltk.corpus.words.words())

def moveEntry(deltaX, deltaY):
    currEntry = window.focus_get()
    currRow, currCol = int(currEntry.grid_info()["row"]), int(currEntry.grid_info()["column"])
    newRow, newCol = currRow + deltaY, currCol + deltaX

    if 0 <= newRow and newRow < 4 and 0 <= newCol and newCol < 4:
        entries[newRow][newCol].focus_set()
    # Continue
    if newCol == 4 and newRow < 3:
        entries[newRow + 1][0].focus_set()
    if newCol == -1 and newRow > 0:
        entries[newRow - 1][3].focus_set()

def arrowMovement(event):
    key = event.keysym

    if key == "Right":
        moveEntry(1, 0)
    elif key == "Left":
        moveEntry(-1, 0)
    elif key == "Down":
        moveEntry(0, 1)
    elif key == "Up":
        moveEntry(0, -1)

window = tk.Tk()
window.geometry("290x310")
window.configure(bg = 'lightgreen')
window.title("Word Hunt Solver")

mainlabel = tk.Label(window, text = "Enter Grid ", font=("Helvetica", 16), height = 0) 
mainlabel.configure(bg = 'lightgreen')

entries = []
for i in range(4):
    rowEntries = []
    for j in range(4):
        entry = tk.Entry(window, width=2, font=("Arial", 40))
        entry.grid(row=i, column=j, padx=5, pady=5)
        rowEntries.append(entry)
    entries.append(rowEntries)

window.bind("<Right>", arrowMovement)
window.bind("<Left>", arrowMovement)
window.bind("<Down>", arrowMovement)
window.bind("<Up>", arrowMovement)

entries[0][0].focus_set()

def submitVals(event):
    #Input Validation
    endTask = False
    for i in range(4):
            for j in range(4):
                if len(entries[i][j].get()) != 1 or not (entries[i][j].get().lower() >= 'a' and entries[i][j].get().lower() <= 'z'):
                    endTask = True
                    break
            if endTask: 
                print("Invalid Inputs. Please try again.")
                break

    tempData = ""
    if not endTask:
        for i in range(4):
            for j in range(4):
                value = str(entries[i][j].get())
                tempData = tempData + value

        window.destroy()

        global data
        data = tempData

window.bind("<Return>", submitVals)

window.mainloop()

print("Input Value: ", data)

# Second Part 
startTime = time.time()
genSet = set()
existingWords = set()
def wordGenerator(currData, word, xCoord, yCoord, val, mapCoord):
    #Assume that max word is 8
    #Convert by doing this data[3 * xCoord + yCoord]
    if currData[4 * xCoord + yCoord] == "X" or val == 8:
        return 
    mapCoord = mapCoord + str(xCoord) + str(yCoord)
    currVal = currData[4 * xCoord + yCoord]
    currData = currData[:4 * xCoord + yCoord] + "X" + currData[4 * xCoord + yCoord + 1:]
    #Do word validation check here. 
    word += currVal
    if len(word) >= 3 and word in englWords and word not in existingWords:
        existingWords.add(word)
        genSet.add((word, mapCoord))

        
    #Loop through all other options
    if (xCoord - 1) >= 0 and (yCoord - 1) >= 0 and not currData[4 * (xCoord - 1) + (yCoord - 1)] == "X":
        dataCPY2 = str(currData)
        wordGenerator(dataCPY2, word, xCoord - 1, yCoord - 1, val + 1, mapCoord)
    if (xCoord - 1) >= 0 and not currData[4 * (xCoord - 1) + (yCoord)] == "X":
        dataCPY2 = str(currData)
        wordGenerator(dataCPY2, word, xCoord - 1, yCoord, val + 1, mapCoord)
    if (xCoord - 1) >= 0 and (yCoord + 1) <= 3 and not currData[4 * (xCoord - 1) + (yCoord + 1)] == "X":
        dataCPY2 = str(currData)
        wordGenerator(dataCPY2, word, xCoord - 1, yCoord + 1, val + 1, mapCoord)   
    if (xCoord + 1) <= 3 and (yCoord + 1) <= 3 and not currData[4 * (xCoord + 1) + (yCoord + 1)] == "X":
        dataCPY2 = str(currData)
        wordGenerator(dataCPY2, word, xCoord + 1, yCoord + 1, val + 1, mapCoord)
    if (xCoord + 1) <= 3 and not currData[4 * (xCoord + 1) + (yCoord)] == "X":
        dataCPY2 = str(currData)
        wordGenerator(dataCPY2, word, xCoord + 1, yCoord, val + 1, mapCoord)
    if (xCoord + 1) <= 3 and (yCoord - 1) >= 0 and not currData[4 * (xCoord + 1) + (yCoord - 1)] == "X":
        dataCPY2 = str(currData)
        wordGenerator(dataCPY2, word, xCoord + 1, yCoord - 1, val + 1, mapCoord)  
    if (yCoord - 1) >= 0 and not currData[4 * (xCoord) + (yCoord - 1)] == "X":
        dataCPY2 = str(currData)
        wordGenerator(dataCPY2, word, xCoord, yCoord - 1, val + 1, mapCoord)
    if (yCoord + 1) <= 3 and not currData[4 * (xCoord) + (yCoord + 1)] == "X":
        dataCPY2 = str(currData)
        wordGenerator(dataCPY2, word, xCoord, yCoord + 1, val + 1, mapCoord) 
    return
for i in range(4):
    for j in range(4):
        dataCPY = str(object=data)  
        wordGenerator(dataCPY,"", i,j, 0, "")

print("\nEnd of Computation")
endTime = time.time()
print("Elapsed Time: {:.2f} seconds".format(endTime - startTime))
sortedList = sorted(genSet, key=lambda x: len(x[0]), reverse=True)
print(sortedList)
Visualizer.mainContents(data, sortedList)

