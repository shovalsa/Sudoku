from random import shuffle, randint
from sudoku.sudoku_matrix import SudokuMatrix
"""
Creates a new random sudoku board file.
"""

class MatrixFileCreator(object):

    def __init__(self):
        self.leanSet = {1,2,3,4,5,6,7,8,9}
        self.bare_list = self.bareList()

    def bareList(self):
        """
        :return: a 2D list where all the numbers are ordered: [[1,2,3...9], [1,2,3...9] ...]
        """
        self.bare_lst = SudokuMatrix("oneToNine.txt")
        return self.bare_lst.mainList

    # def shuffleList(self):
    #     self.shuffledList = self.bare_list[:]
    #     while not(self.bare_lst.evaluateGame(self.shuffledList)):
    #         for item in self.shuffledList:
    #             shuffle(item)
    #     return self.shuffledList

    def shuffleRows(self, lst):
        """
        :param lst: an ordered number list [1, 2, 3, 4, 5, 6, 7, 8, 9]
        :return: a list where the numbers are randomly shuffled, e.g. [5, 3, 4, 6, 7, 8, 9, 1, 2]
        """
        for row in lst:
            shuffle(row)
        return lst

    def shuffleList(self):
        """
        :return: a 2D list where the numbers are randomly shuffled, e.g. [[5, 3, 4, 6, 7, 8, 9, 1, 2], [1, 9, 8, 3, 4, 2, 5, 6, 7],...]
        The returned 2D list makes a valid solved sudoku board.
        """
        self.lst = self.bare_list.copy()
        self.shuffled_list = self.shuffleRows(self.lst)
        while not(self.bare_lst.evaluateGame(self.shuffled_list)):
            self.shuffled_list = self.shuffleRows(self.lst)
        return self.shuffled_list

    def unsolveSudoku(self, lst, difficulty):
        """
        places 0 instead of randomly picked numbers in the new board.
        :param lst: a 2D list of numbers. Potentially the output of shuffleList()
        :param difficulty: a string to mention how difficult the sudoku should be. easy = 3 blanks in each row, 'medium' = 5 blanks and 'hard' = 7 blanks
        :return: a new 2D list with zeros instead of numbers
        """
        dfclty = {'easy':4, 'medium':6, 'hard':8}
        for item in lst:
            for x in range(0,dfclty[difficulty]):
                rand = randint(0,len(item)-1)
                item[rand] = 0
        return lst

    def createNewFile(self, difficulty):
        """
        :param difficulty: a string to mention how difficult the sudoku should be. easy = 3 blanks in each row, 'medium' = 5 blanks and 'hard' = 7 blanks
        :return: a new file with 9 rows, each has 9 numbers. The numbers make a solvable valid sudoku board, e.g.
        003000000
        007400300
        ...
        000000900
        """
        new_sudoku = self.shuffleList()
        unsolved = self.unsolveSudoku(new_sudoku, difficulty)
        file_name = "sudoku_"+ str(unsolved[0])
        with open(file_name, "w") as target:
            for line in unsolved:
                target.write(line)
        return target
