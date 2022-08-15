class Solution(object):
    def robbing(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        prev = nums[0] # i-2
        act = max(nums[0], nums[1]) # i-1
        maxi = act
        for i in range(2, n):
            if prev + nums[i] > act:
                maxi = prev + nums[i]
                prev, act = act, prev + nums[i]
            else:
                maxi = act
                prev = act

        return maxi
    
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        return max(self.robbing(nums[:-1]),self.robbing(nums[1:]))
        