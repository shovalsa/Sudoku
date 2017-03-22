from random import shuffle, randint

class SudokuFileCreator(object):

    def __init__(self):
        self.mainList = self.create_list()
        self.leanSet = {1,2,3,4,5,6,7,8,9}


    def create_list(self):
        self.nineList = []
        for x in range(0, 9):
            subList = []
            self.nineList.append(subList)
            num = 0
            for y in range(0, 9):
                num +=1
                subList.append(num)
        return self.nineList

    def shuffleList(self):
        self.shuffledList = self.mainList[:]
        while not(self.MatrixAnalyzer.check_column(self.shuffledList)) or not((self.MatrixAnalyzer.check_row(self.shuffledList))) or not((self.MatrixAnalyzer.check_boxes(self.shuffledList))):
            for item in self.shuffledList:
                shuffle(item)
        return self.shuffledList

    def unsolveSudoku(self, array):
        for item in array:
            for x in range(0,8):
                rand = randint(0,len(item)-1)
                item[rand] = 0
        return array

    def createNewFile(self):
        new_sudoku = self.shuffleList()
        unsolved = self.unsolveSudoku(new_sudoku)
        file_name = "sudoku_"+ unsolved[0]
        with open("file_name", "w") as target:
            for line in unsolved:
                target.write(line)

