import tkinter as tk
def moveEntry(deltaX, deltaY):
    currEntry = window.focus_get()
    currRow, currCol = int(currEntry.grid_info()["row"]), int(currEntry.grid_info()["column"])
    newRow, newCol = currRow + deltaY, currCol + deltaX

    if 0 <= newRow and newRow < 4 and 0 <= newCol and newCol < 4:
        entries[newRow][newCol].focus_set()

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
window.geometry("400x400")
window.configure(bg = 'lightgreen')
window.title("Word Hunt Solver")

mainlabel = tk.Label(window, text = "Enter Grid ", font=("Helvetica", 16)) 
# mainlabel.pack()
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

window.mainloop()
