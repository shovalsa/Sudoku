from tkinter import *
from shecodes_execises.sudoku.sudoku_matrix import SudokuMatrix
# from shecodes_execises.sudoku.board_display import BoardDisplay
from shecodes_execises.sudoku.sudoku_game import SudokuGame

matrix_003000000 = SudokuMatrix("sudoku_003000000.txt")
print(matrix_003000000.mainList)
exemplar = [[4,2,3,9,5,6,1,7,8], [5,9,7,4,8,1,3,2,6], [8,6,1,7,3,2,4,5,9], [6,1,9,5,7,3,2,8,4], [2,3,8,6,1,4,5,9,7], [7,4,5,8,2,9,6,3,1], [1,5,6,2,9,7,8,4,3], [9,8,4,3,6,5,7,1,2], [3,7,2,1,4,8,9,6,5]]

# print(matrix_003000000.createAllRows(exemplar))
new_game = SudokuGame(matrix_003000000) # this line is enough to start the board
# new_game.GUI
# root= Tk()
# new_board = BoardDisplay(matrix_210000400, root)
# print("initial board:", matrix_210000400.mainList, "\n")
# print("boxed board: ", new_board.allBoxes, "\n")
# # print("rows board: ", new_game.getEntries(), "\n")
#
# # new_board.display_game()
# root.mainloop()