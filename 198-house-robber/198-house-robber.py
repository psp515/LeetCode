class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        # f[i] - maksymalny zysk z kradziezy do i-tego domu
        f = [0 for _ in range(n)]
        f[0] = nums[0]
        f[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            f[i] = max(nums[i]+ f[i-2], f[i-1])
            
        return f[-1]