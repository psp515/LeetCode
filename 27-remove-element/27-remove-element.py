
import heapq

class Solution(object):
    
    def removeElement(self, nums, val):
        
        n = len(nums)
        i,j = 0, n - 1
        count = 0
        
        while i < j:
            if nums[i] == val :
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
                
        
        for element in nums:
            if element != val:
                count +=1
        
        return count
        