class Solution(object):
    def diagonalSum(self, mat):
        n = len(mat)
    
        visited = [[False for _ in range(n)] for _ in range(n)]
        sum = 0
        i,j = 0,0
        
        while i < n and j < n:
            if not visited[i][j]:
                visited[i][j] = True
                sum += mat[i][j]
            i+=1
            j+=1
        
        i, j = n - 1, 0
        
        while i >= 0 and j < n:
            if not visited[i][j]:
                visited[i][j] = True
                sum += mat[i][j]
            i -= 1
            j += 1
            
        return sum
        