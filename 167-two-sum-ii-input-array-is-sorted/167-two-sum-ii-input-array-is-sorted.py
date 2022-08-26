class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        
        i, j = 0, n - 1
        
        while i < j:
            sum = nums[i] + nums[j]
            if sum == target:
                return [ i + 1, j + 1]
            elif sum < target:
                i += 1
            else:
                j -= 1
            
            
        return None
        