from tkinter import *
from sudoku.sudoku_matrix import SudokuMatrix
from sudoku.board_display import BoardDisplay


class Evaluator(object):
    def __init__(self, board):
        self.board = board
        self.newRows = self.createAllRows(self.board.initialBoard)
        self.solvedBoard = self.getEntries()

    def boxToRow(self, array, row, column):
        self.boxList = []
        num_1 = row
        for x in range(0,3):
            num_2 = column
            for y in range(0,3):
                self.boxList.append(array[num_1][num_2])
                num_2+=1
            num_1+=1
        return self.boxList

    def createAllRows(self, array):
        rowIndex = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        self.listOfRows = []
        for item in rowIndex:
            self.listOfRows.append(self.boxToRow(array, item[0], item[1]))
        return self.listOfRows

    def getEntries(self):
        self.solvedSudoku = []
        for item in self.newRows:
            if type(item) is Entry:
                self.solvedSudoku.append(item['textvariable'])
            elif type(item) is Label:
                self.solvedSudoku.append(item['text'])
        return self.solvedSudoku


    def clearAll(self):
        print("cleared!")

    def evaluateGame(self):
        pass