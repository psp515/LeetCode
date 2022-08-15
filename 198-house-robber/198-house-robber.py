class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        # f[i] - maksymalny zysk z kradziezy do i-tego domu
        f = [0 for _ in range(n)]
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