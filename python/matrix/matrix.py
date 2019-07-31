class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split('\n')  # Separate rows
        self.matrix = [self.matrix[i].split(' ') for i in range(len(self.matrix))]  # Separate numbers in each row
        self.matrix = [[int(i) for i in j] for j in self.matrix]  # Convert string numbers to int

    def row(self, index):
        """ Returns matrix row by index"""
        return self.matrix[index-1]

    def column(self, index):
        """ Returns matrix column by index"""
        return [self.matrix[i][index-1] for i in range(len(self.matrix))]

