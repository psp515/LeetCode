class Solution(object):
    def searchMatrix(self, matrix, target):
        n,m = len(matrix), len(matrix[0])
        
        for i in range(n):
            if matrix[i][-1] >= target:
                for j in range(m):
                    if matrix[i][j] == target: 
                        return True
                
                return False
        
        return False
        
        