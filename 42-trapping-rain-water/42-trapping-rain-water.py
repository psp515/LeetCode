class Solution(object):
    def trap(self, height):
        n = len(height)
        max_left = [0 for _ in range(n)]
        max_left[-1] = height[-1]
        max_right = [0 for _ in range(n)]
        max_right[0] = height[0]
        
        for i in range(1, n):
            max_right[i] = max(max_right[i-1], height[i])
        
        for i in range(n-2,-1,-1):
            max_left[i] = max(max_left[i+1], height[i])
            
        sum = 0
        
        for i in range(n):
            sum += min(max_left[i], max_right[i]) - height[i]
        
        return sum
            
            
        