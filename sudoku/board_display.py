from tkinter import *
from shecodes_execises.sudoku.sudoku_matrix import SudokuMatrix
# from shecodes_execises.sudoku.sudoku_game import SudokuGame
from shecodes_execises.sudoku.evaluator import Evaluator
from tkinter import messagebox


class BoardDisplay(Frame):
    def __init__(self, sMatrix, master=None):
        Frame.__init__(self, master)
        self.master = master # the main frame, like root
        self.allBoxes = sMatrix.allBoxes
        self.lst = []
        self.grid() # or pack or place
        self.display_game()
        self.displayButtons()
        self.sMatrix = sMatrix
        self.solvedBoard = self.solvedSudoku()

    def display_game(self):
        for subList in self.setEntries():
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
                    new_entry = Entry(new_frame, textvariable=blank, width=5)
                    # new_entry.delete(0, END)
                    array.append(new_entry)
                    self.lst.append(blank)
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
        Button(buttonsFrame, text="Reset table", bg="red", command=self.clear_board).pack(side=LEFT, ipadx=4, ipady=5)
        Button(buttonsFrame, text="Submit answer", bg="green", command=self.success_or_failure).pack(side=RIGHT, ipadx=4, ipady=5)

    def success_or_failure(self):
        temp = self.solvedSudoku()
        print(self.solvedBoard)
        rows = self.sMatrix.createAllRows(temp)
        print(rows)
        if self.sMatrix.evaluateGame(rows):
            messagebox.showinfo("Result", "Congratulations! you have solved the sudoku board correctly!.")
            print("success")
        else:
            print("failure")
            messagebox.askokcancel("Result", "Your solution does not meet the requirements for a sudoku game."
                                             " Please choose 'cancel' to retry.")

    def solvedSudoku(self):
        x = 0
        self.solved_sudoku = []
        for item in self.setEntries():
            subList = []
            for subItem in item:
                if type(subItem) is Entry:
                    # print(subItem['textvariable'])
                    subList.append(self.lst[x].get()) #subItem['textvariable'])
                    x += 1
                elif type(subItem) is Label:
                    subList.append(subItem['text'])
            self.solved_sudoku.append(subList)
        return self.solved_sudoku

    def clear_board(self):
        self.new_board = BoardDisplay(self.sMatrix, self.master)
