class Solution(object):
    def is_closed_island(self, grid, i, j):
        n, m = len(grid), len(grid[0])
        stack = [(i, j)]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        is_island = True
        counter = 0
        
        while stack:
            r, c = stack.pop()
            if grid[r][c] == 1 and (r == 0 or c == 0 or r == n-1 or c == m-1):
                is_island = False
            
            if grid[r][c] == 1:
                counter += 1
                
            grid[r][c] = 0
            
            for dr, dc in dirs:
                new_r, new_c = r+dr, c+dc
                if 0 <= new_r < n and 0 <= new_c < m and grid[new_r][new_c] == 1:
                    stack.append([new_r, new_c])
        
        return is_island, counter
        
    def numEnclaves(self, grid):
        n, m = len(grid), len(grid[0])
        closed_islands = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                isi, c = self.is_closed_island(grid, i, j)
                if isi:
                    closed_islands += c
        
        return closed_islands