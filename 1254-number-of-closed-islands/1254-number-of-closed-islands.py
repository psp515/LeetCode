class Solution(object):
    def is_closed_island(self, grid, i, j):
        n, m = len(grid), len(grid[0])
        stack = [(i, j)]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        is_island = True
        while stack:
            r, c = stack.pop()
            if grid[r][c] == 0 and (r == 0 or c == 0 or r == n-1 or c == m-1):
                is_island = False
            
            grid[r][c] = 1
            
            for dr, dc in dirs:
                new_r, new_c = r+dr, c+dc
                if 0 <= new_r < n and 0 <= new_c < m and grid[new_r][new_c] == 0:
                    stack.append([new_r, new_c])
        
        return is_island
        
    def closedIsland(self, grid):
        n, m = len(grid), len(grid[0])
        closed_islands = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    continue
                
                if self.is_closed_island(grid, i, j):
                    closed_islands += 1
        
        return closed_islands
                
        
        