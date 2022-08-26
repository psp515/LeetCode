class Solution(object):
    def countNegatives(self, grid):
        counter = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    counter += 1
        
        return counter