class NumMatrix(object):

    def __init__(self, matrix):
        n,m = len(matrix), len(matrix[0])
        self.matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                self.matrix[i+1][j+1]= matrix[i][j] + self.matrix[i][j+1] + self.matrix[i+1][j] - self.matrix[i][j]
        

    def sumRegion(self, row1, col1, row2, col2):
        return self.matrix[row2+1][col2+1] - self.matrix[row1][col2+1] - self.matrix[row2+1][col1] + self.matrix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)