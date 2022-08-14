class Solution(object):
    def minimumOperations(self, nums):
        count = 0
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue
            x = nums[i]
            for j in range(i, n):
                nums[j] -= x
            count += 1
            
        
        return count
        