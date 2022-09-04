class Solution(object):
    def combinationSum4(self, nums, target):
        nums.sort()

        if target < nums[0]:
            return 0
        n = target + 1
        f = [0 for _ in range(n)]

        for i in range(1, n):
            for j in range(len(nums)):
                if i - nums[j] == 0:
                    f[i] += 1
                elif i - nums[j] > 0:
                    f[i] += f[i - nums[j]]

        return f[-1]