class Solution(object):
    def maximumUniqueSubarray(self, nums):
        d = {}
        n = len(nums)
        j = 0
        maxs = 0
        act_sum = 0
        for i in range(n):
            val = nums[i]
            if not val in d:
                d[val] = 1
                act_sum += val
            else:
                d[val] += 1
                act_sum += val
                
                while d[val] == 2:
                    val2 = nums[j]
                    d[val2] -= 1
                    j += 1
                    act_sum -= val2
                    
            maxs = max(maxs, act_sum)

        return maxs
        