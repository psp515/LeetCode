class Solution(object):
    def validate(self,i, min, max):
        if i < min:
            return False
        
        if i >= max:
            return False
        
        return True
        
    
    def DFSarea(self, grid, i, j, visited):
        area = 0
        stack = [(i,j)]
        
        while stack:
            x,y = stack.pop()
            
            if not self.validate(x, 0, len(grid)) or not self.validate(y, 0, len(grid[0])):
                continue
            
            if visited[x][y]:
                continue
            
            if grid[x][y] == 1:
                area += 1
                stack.append((x,y - 1))          
                stack.append((x,y + 1))
                stack.append((x - 1,y))
                stack.append((x + 1,y))
            
            visited[x][y] = True
        
        return area
            
    def maxAreaOfIsland(self, grid):
        n, m = len(grid), len(grid[0])
        
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        maxarea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0: 
                    visited[i][j] = True
                if visited[i][j] == False:
                    maxarea = max(maxarea, self.DFSarea(grid, i, j, visited))
        
        return maxarea