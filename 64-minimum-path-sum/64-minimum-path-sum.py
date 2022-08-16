class Solution(object):
    def minPathSum(self, grid):
        n,m = len(grid), len(grid[0])
        # f[i][j] - minimal cost to get to the i-th field
        f = [[0 for _ in range(m)] for _ in range(n )]
        
        f[0][0] = grid[0][0]
        
        for i in range(1,n):
            f[i][0] = f[i-1][0] + grid[i][0]
        
        for j in range(1,m):
            f[0][j] = f[0][j-1] + grid[0][j]
        
        for i in range(1, n):
            for j in range(1, m):
                    f[i][j] = min(f[i-1][j],f[i][j-1]) + grid[i][j]
        
        return f[-1][-1]