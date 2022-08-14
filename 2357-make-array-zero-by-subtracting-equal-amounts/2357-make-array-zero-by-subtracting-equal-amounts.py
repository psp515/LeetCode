class Solution(object):
    def minimumOperations(self, nums):
        count = 0
        nums.sort()
        value = 0
        n = len(nums)
        for i in range(n):
            if nums[i] - value == 0:
                continue
            value = nums[i]
            count += 1
            
        
        return count
        