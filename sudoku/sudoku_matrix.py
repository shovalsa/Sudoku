from random import shuffle, randint

class SudokuMatrix(object):

    def __init__(self, source_file):
        self.source_file = source_file
        self.mainList = self.extract_list()
        self.leanSet = {1,2,3,4,5,6,7,8,9}
        # self.cubeList = self.createAllBoxes(self.mainList)

    def extract_list(self):
        self.new_list = []
        with open(self.source_file, "r") as source:
            for line in source.readlines():
                subList = []
                for char in line:
                    if not(char == "\n"):
                        subList.append(int(char))
                self.new_list.append(subList)
        return self.new_list


    def create_box(self, array, row, column):
        self.boxList = []
        num_1 = row
        for x in range(0,3):
            num_2 = column
            for y in range(0,3):
                self.boxList.append(array[num_1][num_2])
                num_2+=1
            num_1+=1
        return self.boxList

    def check_row(self, array):
        num = 0
        for item in array:
            if set(item) != self.leanSet:
                num +=1
        return num == 0

    def create_column(self, array, column):
        self.columnList = []
        for item in array:
            self.columnList.append(item[column])
        return self.columnList

    def check_column(self, array):
        num = 0
        for x in range(0,len(array)):
            if set(self.create_column(array, x)) != self.leanSet:
                num +=1
        return num == 0

    def check_boxes(self, array):
        boxIndex = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        num = 0
        for item in boxIndex:
            if set(self.create_box(array, item[0], item[1])) != self.leanSet:
                num +=1
        return num == 0

    def createAllBoxes(self, array):
        boxIndex = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        self.listOfBoxes = []
        for item in boxIndex:
            self.listOfBoxes.append(self.create_box(array, item[0], item[1]))
        return self.listOfBoxes