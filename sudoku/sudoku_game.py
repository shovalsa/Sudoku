from tkinter import *
# from sudoku.board_display import BoardDisplay
# from sudoku.sudoku_matrix import SudokuMatrix
from tkinter import messagebox
from random import randint
class SudokuMatrix(object):

    def __init__(self, source_file):
        self.source_file = source_file
        self.mainList = self.extract_list()
        self.leanSet = {1,2,3,4,5,6,7,8,9}


    def extract_list(self):
        """
        takes the numbers from a file and creates a 2D list
        :returns a list of numbers that make a solvable sudoku board.
        """
        self.new_list = []
        with open(self.source_file, "r") as source:
            for line in source.readlines():
                subList = []
                for char in line:
                    if not(char == "\n"):
                        subList.append(int(char))
                self.new_list.append(subList)
        return self.new_list


    def create_box(self, lst, row, column):
        """
        creates a single list box from a given rowXcolumn.
        given the following 2D list,
        boxIndex = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        :row: boxIndex[0]
        :column: boxIndex[1]
        :return: A 2D list which represents one box of a sudoku game.
        """
        self.boxList = []
        num_1 = row
        for x in range(0,3):
            num_2 = column
            for y in range(0,3):
                self.boxList.append(lst[num_1][num_2])
                num_2+=1
            num_1+=1
        return self.boxList


    def create_column(self, lst, column):
    # creates a single column lst from a given row, e.g. [a[0], b[0]... n[0]]
        self.columnList = []
        for item in lst:
            self.columnList.append(item[column])
        return self.columnList

    def createAllBoxes(self, lst):
        # creats a 2D lst of all the box created with create_box()
        boxIndex = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        self.listOfBoxes = []
        for item in boxIndex:
            self.listOfBoxes.append(self.create_box(lst, item[0], item[1]))
        return self.listOfBoxes


    def boxToRow(self, lst, row, column):
        # the opposite of create_box() - creates a single row lst from a given box lst.
        self.boxList = []
        num_1 = row
        for x in range(0,3):
            num_2 = column
            for y in range(0,3):
                self.boxList.append(lst[num_1][num_2])
                num_2+=1
            num_1+=1
        return self.boxList

    def createAllRows(self, lst):
        # creates a 2D lst from all the rows created with boxToRow()
        rowIndex = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        self.listOfRows = []
        for item in rowIndex:
            self.listOfRows.append(self.boxToRow(lst, item[0], item[1]))
        return self.listOfRows

    def check_row(self, lst):
        num = 0
        for item in lst:
            if set(item) != self.leanSet:
                num +=1
        return num == 0


    def check_column(self, lst):
        num = 0
        for x in range(0,len(lst)):
            if set(self.create_column(lst, x)) != self.leanSet:
                num +=1
        return num == 0

    def check_boxes(self, lst):
        boxIndex = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        num = 0
        for item in boxIndex:
            if set(self.create_box(lst, item[0], item[1])) != self.leanSet:
                num +=1
        return num == 0

    def evaluateGame(self, lst):
        return (self.check_row(lst)) and (self.check_column(lst)) and (self.check_boxes(lst))


class BoardDisplay(Frame):
    def __init__(self, sMatrix, master=None):
        Frame.__init__(self, master)
        self.master = master # the main frame, like root
        self.lst = []
        self.grid()
        self.sMatrix = sMatrix

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
        self.displayButtons()

    def setEntries(self):
        boxIndex = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        self.matrixCopy = []
        item = 0
        for subList in self.sMatrix.createAllBoxes(self.sMatrix.mainList):
            new_frame = Frame(self.master, bd=5, relief=RIDGE)
            new_frame.grid(row=boxIndex[item][0], column=boxIndex[item][1])
            item +=1
            lst = []
            for number in subList:
                if number == 0:
                    blank = IntVar()
                    new_entry = Entry(new_frame, textvariable=blank, width=5)
                    # new_entry.delete(0, END)
                    lst.append(new_entry)
                    self.lst.append(blank)
                else:
                    lst.append(Label(new_frame, text=number))
            self.matrixCopy.append(lst)
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
        rows = self.sMatrix.createAllRows(temp)
        if self.sMatrix.evaluateGame(rows):
            messagebox.showinfo("Result", "Congratulations! you have solved the sudoku board correctly!.")
            print("success")
        else:
            print("failure")
            messagebox.showinfo("Result", "Your solution does not meet the\n requirements for a sudoku game.\n"
                                             "Try again!")

    def solvedSudoku(self):
        x = 0
        is_exception = False
        self.solved_sudoku = []
        for item in self.setEntries():
            subList = []
            for subItem in item:
                if type(subItem) is Entry:
                    try:
                        subList.append(self.lst[x].get())
                        x += 1
                    except:
                        is_exception = True
                elif type(subItem) is Label:
                    subList.append(subItem['text'])
            self.solved_sudoku.append(subList)
        if is_exception == True:
            self.callback()
        else:
            return self.solved_sudoku

    def clear_board(self):
        self.new_board = BoardDisplay(self.sMatrix, self.master)
        self.new_board.display_game()

    def callback(self):
        messagebox.showinfo("Error", "Make sure that the entire board \nis filled with numbers (in digits).")

"""
This class initiates the game. In the future we can add tools here like leaderboard, strategies, statistics etc.
"""
class SudokuGame(object):
    def __init__(self, sourceFile):
        self.matrix = SudokuMatrix(sourceFile) # sourceFile is a file containing lines of numbers.
        # self.GUI = self.create_GUI()

    def unsolveSudoku(self, difficulty="easy"):
        """
        places 0 instead of randomly picked numbers in the new board.
        :param lst: a 2D list of numbers. Potentially the output of shuffleList()
        :param difficulty: a string to mention how difficult the sudoku should be. easy = 3 blanks in each row, 'medium' = 5 blanks and 'hard' = 7 blanks
        :return: a new 2D list with zeros instead of numbers
        """
        dfclty = {'easy':4, 'medium':6, 'hard':8}
        for item in self.matrix.mainList:
            for x in range(0,dfclty[difficulty]):
                rand = randint(0,len(item)-1)
                item[rand] = 0
        return self.matrix

    def create_GUI(self):
        root= Tk()
        self.new_board = BoardDisplay(self.matrix, root)
        self.new_board.display_game()
        root.mainloop()
        # return self.new_board

    def leaderBoard(self):
        pass
