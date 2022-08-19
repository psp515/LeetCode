class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        f = [False for _ in range(n)]
        f[0] = True
        for j in range(nums[0]):
            if j + 1 < n:
                f[j + 1] = True

        for i in range(1, n):
            if f[i]:
                for j in range(nums[i]):
                    if i + j + 1 < n:
                        f[i + j + 1] = True
            if f[-1]:
                return True

        return f[-1]
                
        