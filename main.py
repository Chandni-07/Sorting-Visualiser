from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quickSort import quick_sort
from insertionSort import insertion_sort
from selectionSort import selection_sort
from mergeSort import merge_sort
from heapSort import heapSort
from waveSort import sortInWave

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

#variables
selected_alg = StringVar()
data = []



def drawData(data,colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 15
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()


def Generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))
    drawData(data, ['blue' for x in range(len(data))])

def StartAlgorithm():

    global data
    if not data: return

    if algMenu.get() == 'Select':
        Label(UI_frame, text="Time Complexity ",bg='White').grid(row=0, column=2, padx=5, pady=5, sticky=W)

    if algMenu.get() == 'Quick Sort':
        Label(UI_frame, text="T(n)  =   O(nlogn)  ",bg='White').grid(row=0, column=2, padx=5, pady=5, sticky=W)
        quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())
        
        

    elif algMenu.get() == 'Bubble Sort':
        Label(UI_frame, text=" T(n)  =   O(n^2)  ",bg='White').grid(row=0, column=2, padx=5, pady=5, sticky=W)
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Selection Sort':
        Label(UI_frame, text=" T(n)  =   O(n^2)  ",bg='White').grid(row=0, column=2, padx=5, pady=5, sticky=W)
        selection_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Insertion Sort':
        Label(UI_frame, text=" T(n)  =   O(n^2)  ",bg='White').grid(row=0, column=2, padx=5, pady=5, sticky=W)
        insertion_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        Label(UI_frame, text=" T(n)  =   O(nlogn)  ",bg='White').grid(row=0, column=2, padx=5, pady=5, sticky=W)
        merge_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Heap Sort':
        Label(UI_frame, text=" T(n)  =   O(nlogn)  ",bg='White').grid(row=0, column=2, padx=5, pady=5, sticky=W)
        heapSort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Wave Sort':
        Label(UI_frame, text=" T(n)   =      O(n)  ",bg='White').grid(row=0, column=2, padx=5, pady=5, sticky=W)
        sortInWave(data, drawData, speedScale.get())

    


#frame / base lauout
UI_frame = Frame(root, width= 600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Select','Bubble Sort', 'Merge Sort','Quick Sort','Selection Sort','Insertion Sort','Heap Sort','Wave Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)


if algMenu.get() == 'Select':
    Label(UI_frame, text="Time Complexity ",bg='White').grid(row=0, column=2, padx=5, pady=5, sticky=W)
       



speedScale = Scale(UI_frame, from_=0.1, to=4.0, length=150, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=3, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=4, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='red').grid(row=1, column=3, padx=5, pady=5)
root.mainloop()