import tkinter as tk
import copy
import nltk

# Add this back for first time users
# nltk.download('words')
englWords = set(nltk.corpus.words.words())


def moveEntry(deltaX, deltaY):
    currEntry = window.focus_get()
    currRow, currCol = int(currEntry.grid_info()["row"]), int(currEntry.grid_info()["column"])
    newRow, newCol = currRow + deltaY, currCol + deltaX
    # print(newRow, newCol)

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
window.geometry("290x350")
window.configure(bg = 'lightgreen')
window.title("Word Hunt Solver")

mainlabel = tk.Label(window, text = "Enter Grid ", font=("Helvetica", 16), height = 0) 
# mainlabel.place(x=0, y=2)
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

data = []
def submitVals():
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
     
    if not endTask:
        for i in range(4):
            rowData = []
            for j in range(4):
                value = entries[i][j].get()
                rowData.append(value)
            data.append(rowData)

        for row in data:
            print(row)
        window.destroy()

submit_button = tk.Button(window, text="Submit", command=submitVals)
submit_button.grid(row=5, column=0, columnspan=4, pady=10)

window.mainloop()

# Second Part 

dataCPY = copy.deepcopy(data)
genSet = []
def wordGenerator(currData, word, xCoord, yCoord, val):
    if currData[xCoord][yCoord] == "X" or val == 10:
        return 
    # print(len(word))
    currVal = currData[xCoord][yCoord]
    currData[xCoord][yCoord] = "X"
    #Do word validation check here. 
    word += currVal
    if len(word) >= 3 and word in englWords:
        genSet.append(word)
    # print(word)
    # print(currData)
        
    #Loop through all other options
    if (xCoord - 1) >= 0 and (yCoord - 1) >= 0 and not currData[xCoord - 1][yCoord - 1] == "X":
        dataCPY2 = copy.deepcopy(currData)
        wordGenerator(dataCPY2, word, xCoord - 1, yCoord - 1, val + 1)
    if (xCoord - 1) >= 0 and not currData[xCoord - 1][yCoord] == "X":
        dataCPY2 = copy.deepcopy(currData)
        wordGenerator(dataCPY2, word, xCoord - 1, yCoord, val + 1)
    if (xCoord - 1) >= 0 and (yCoord + 1) <= 3 and not currData[xCoord - 1][yCoord + 1] == "X":
        dataCPY2 = copy.deepcopy(currData)
        wordGenerator(dataCPY2, word, xCoord - 1, yCoord + 1, val + 1)   
    if (xCoord + 1) <= 3 and (yCoord + 1) <= 3 and not currData[xCoord + 1][yCoord + 1] == "X":
        dataCPY2 = copy.deepcopy(currData)
        wordGenerator(dataCPY2, word, xCoord + 1, yCoord + 1, val + 1)
    if (xCoord + 1) <= 3 and not currData[xCoord + 1][yCoord] == "X":
        dataCPY2 = copy.deepcopy(currData)
        wordGenerator(dataCPY2, word, xCoord + 1, yCoord, val + 1)
    if (xCoord + 1) <= 3 and (yCoord - 1) >= 0 and not currData[xCoord + 1][yCoord - 1] == "X":
        dataCPY2 = copy.deepcopy(currData)
        wordGenerator(dataCPY2, word, xCoord + 1, yCoord - 1, val + 1)  
    if (yCoord - 1) >= 0 and not currData[xCoord][yCoord - 1] == "X":
        dataCPY2 = copy.deepcopy(currData)
        wordGenerator(dataCPY2, word, xCoord, yCoord - 1, val + 1)
    if (yCoord + 1) <= 3 and not currData[xCoord][yCoord + 1] == "X":
        dataCPY2 = copy.deepcopy(currData)
        wordGenerator(dataCPY2, word, xCoord, yCoord + 1, val + 1) 
    return
        
wordGenerator(dataCPY,"", 0,0, 0)
print("hi")
print(genSet)

