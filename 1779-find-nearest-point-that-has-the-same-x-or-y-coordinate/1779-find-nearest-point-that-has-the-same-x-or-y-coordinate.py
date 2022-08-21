class Solution(object):
    
    def manhattan(self, x1, x2, y1, y2):
        return abs(x2 - x1) + abs(y2 - y1)
        
    
    def nearestValidPoint(self, x, y, points):
        index = -1
        min_dist = float('inf')
        
        for i in range(len(points)):
            x1,y1 = points[i]
            if x1 == x or y1 == y:
                dist = self.manhattan(x, x1, y, y1)
                if dist < min_dist:
                    min_dist = dist
                    index = i
        
        
        return index
        