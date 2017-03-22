from tkinter import *
from sudoku.sudoku_matrix import SudokuMatrix
# from sudoku.game import Game


class BoardDisplay(Frame):
    def __init__(self, sMatrix, master=None):
        Frame.__init__(self, master)
        self.master = master # the main frame, like root
        self.allBoxes = sMatrix.createAllBoxes(sMatrix.mainList)
        self.initialBoard = self.setEntries()
        self.grid() # or pack or place
        self.display_game()
        # self.displayButtons()

    def display_game(self):
        for subList in self.initialBoard:
            xRow = 0
            position = 0
            for x in range(0,3):
                xColumn = 0
                for y in range(0,3):
                    subList[position].grid(row=xRow, column=xColumn, ipadx=2, ipady=2)
                    xColumn+=1
                    position+=1
                xRow +=1


    def setEntries(self):
        boxIndex = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        self.matrixCopy = []
        item = 0
        for subList in self.allBoxes:
            new_frame = Frame(self.master, bd=5, relief=RIDGE)
            new_frame.grid(row=boxIndex[item][0], column=boxIndex[item][1])
            item +=1
            array = []
            for number in subList:
                if number == 0:
                    blank = IntVar()
                    array.append(Entry(new_frame, textvariable=blank, width=5))
                else:
                    array.append(Label(new_frame, text=number))
            self.matrixCopy.append(array)
        return self.matrixCopy


    def create_frame(self):
        boxIndex = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        for item in boxIndex:
            new_frame = Frame(self.master, bd=5, relief=RIDGE)
            new_frame.grid(row=item[0], column=item[1])

    def displayButtons(self):
        buttonsFrame = Frame(self.master)
        buttonsFrame.grid(row=12, columnspan=5, sticky=N)
        clear = Button(buttonsFrame, text="Clear table", bg="red", command=Game.clearAll).pack(side=LEFT, ipadx=4, ipady=5)
        submit = Button(buttonsFrame, text="Submit answer", bg="green", command=Game.evaluateGame).pack(side=RIGHT, ipadx=4, ipady=5)

