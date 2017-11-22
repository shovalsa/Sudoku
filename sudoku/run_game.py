from sudoku.sudoku_game import SudokuGame
from sudoku.matrix_file_creator import MatrixFileCreator

def start_game(file_name=None, unsolved=True, difficulty='medium'):
    """
    Initiates a solvable board game GUI
    :param file_name: a txt file with 9 rows of 9 numbers each.
            IMPORTANT:
             1. The numbers should form a valid sudoku game.
             2. In case the board is not solved (has blanks), each blank should be represented by a 0 (zero).
             3. Leaving this parameter with None will create a random solvable board. This process is extremely
                long, heavy and generally not recommended.
    :param unsolved: In case a txt file is provided, is the board already solved or with blanks.
    :param difficulty: a string to mention how difficult the sudoku should be. easy = 3 blanks in each row,
                       'medium' = 5 blanks and 'hard' = 7 blanks
    :return: A 2D list of unsolved game, for a game GUI to present.
    """
    if (file_name == None):
        new_game = MatrixFileCreator()
        try:
            file_name = new_game.createNewFile(difficulty)
        except:
            file_name = new_game.createNewFile('medium')
    elif unsolved == True:
        new_game = SudokuGame(file_name)
    else:
        new_game = SudokuGame(file_name)
        try:
            new_game.unsolveSudoku(difficulty)
        except:
            new_game.unsolveSudoku(difficulty='medium')
    return new_game


new = start_game("sudoku_003000000.txt")
new.create_GUI()