class Solution(object):
    def validate(self, index, maxi):
        if index < 0:
            return False
        if index >= maxi:
            return False
        return True
    
    def isSubIsland(self, grid, common, i, j):
        stack = [(i, j)]
        is_usb = True
        while stack:
            x, y = stack.pop()

            # 0 - 1 action can't happen

            if grid[x][y] == 0 and common[x][y] == 0:
                continue

            if grid[x][y] == 1 and common[x][y] == 0:
                is_usb = False

            if self.validate(x - 1, self.n) and grid[x - 1][y] == 1:
                stack.append((x - 1, y))

            if self.validate(x + 1, self.n) and grid[x + 1][y] == 1:
                stack.append((x + 1, y))

            if self.validate(y - 1, self.m) and grid[x][y - 1] == 1:
                stack.append((x, y - 1))

            if self.validate(y + 1, self.m) and grid[x][y + 1] == 1:
                stack.append((x, y + 1))

            grid[x][y] = 0
            common[x][y] = 0

        return is_usb
    
    def countSubIslands(self, grid1, grid2):
        self.n, self.m = len(grid1), len(grid1[0])
        
        common = [[0 for _ in range(self.m)] for _ in range(self.n)]
        subislands = 0
        
        for i in range(self.n):
            for j in range(self.m):
                if grid2[i][j] == 1 and grid1[i][j] == 1:
                    common[i][j] = 1
        
        for i in range(self.n):
            for j in range(self.m):
                if common[i][j] == 0:
                    continue
                    
                if grid2[i][j] == 1:
                    if self.isSubIsland(grid2, common, i, j):
                        subislands += 1 
        
        return subislands
        