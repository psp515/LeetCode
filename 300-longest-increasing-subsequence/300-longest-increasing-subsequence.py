class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1 for _ in range(n)]
        
        for i in range(n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    f[i] = max(f[j]+1, f[i])
        
        return max(f)