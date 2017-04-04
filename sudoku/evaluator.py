from tkinter import *
from shecodes_execises.sudoku.sudoku_matrix import SudokuMatrix
# from shecodes_execises.sudoku.board_display import BoardDisplay


class Evaluator(object):

    def __init__(self):
        # self.newRows = SudokuMatrix.createAllRows(self.board.initialBoard)
        self.leanSet = {1,2,3,4,5,6,7,8,9}


    def check_row(self, array):
        num = 0
        for item in array:
            if set(item) != self.leanSet:
                num +=1
        return num == 0


    def check_column(self, array):
        num = 0
        for x in range(0,len(array)):
            if set(SudokuMatrix.create_column(array, x)) != self.leanSet:
                num +=1
        return num == 0

    def check_boxes(self, array):
        boxIndex = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        num = 0
        for item in boxIndex:
            if set(SudokuMatrix.create_box(array, item[0], item[1])) != self.leanSet:
                num +=1
        return num == 0


    def evaluateGame(self, array):
        return (self.check_row(array)) and (self.check_column(array)) and (self.check_boxes(array))


