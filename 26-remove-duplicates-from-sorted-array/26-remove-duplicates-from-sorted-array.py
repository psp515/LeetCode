
class Solution(object):
    
    def removeDuplicates(self, nums):
        count = 0 
        prev = -101 # assume this is -math.inf
        for i in range(len(nums)):
            if nums[i] != prev:
                prev = nums[i]
                nums[count] = nums[i]
                count+=1
                
        return count
        