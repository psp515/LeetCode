class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        f = [[float('inf') for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            f[0][i] = matrix[0][i]
        
        for i in range(1, n):
            for j in range(n):
                nj = j
                f[i][j] = f[i-1][nj] + matrix[i][j]
                
                
                nj = j - 1
                if nj >= 0: 
                    f[i][j] = min(f[i-1][nj] + matrix[i][j] , f[i][j])
                nj = j + 1 
                if nj < n: 
                    f[i][j] = min(f[i-1][nj] + matrix[i][j] , f[i][j])
        
        return min(f[-1])