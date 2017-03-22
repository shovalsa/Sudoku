from tkinter import *
from sudoku.sudoku_matrix import SudokuMatrix
from sudoku.board_display import BoardDisplay
from sudoku.evaluator import Evaluator

matrix_210000400 = SudokuMatrix("sudoku_210000400")
# print(matrix_210000400.mainList)

root= Tk()
new_board = BoardDisplay(matrix_210000400, root)
# new_game = Game(new_board)
print("initial board:", matrix_210000400.mainList, "\n")
print("boxed board: ", new_board.allBoxes, "\n")
# print("rows board: ", new_game.getEntries(), "\n")

# new_board.display_game()
root.mainloop()