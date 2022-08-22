import heapq

class Solution(object):
    def jump(self, nums):
        output = 0
        idx = 0
        if len(nums) == 1: 
            return 0
        
        while True:
            currentNum = nums[idx]
            currentMax, currentIdx = 0, 0
            for t in range(1, currentNum + 1):
                if idx + t >= len(nums) - 1: 
                    return output + 1
                if idx + t + nums[idx+t] >= currentMax + currentIdx:
                    currentMax = nums[idx+t]
                    currentIdx = idx + t
            idx = currentIdx
            output += 1
        
        return output 
        