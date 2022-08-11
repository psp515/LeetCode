class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        
        nums = [(nums[i], i) for i in range(n)]
        
        nums.sort(key = lambda x:x[0])
        
        i, j = 0, n - 1
        
        while i < j:
            sum = nums[i][0] + nums[j][0]
            if sum == target:
                return [nums[i][1], nums[j][1]]
            elif sum < target:
                i += 1
            else:
                j -= 1
            
            
        return None
        
        