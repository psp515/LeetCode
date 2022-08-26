class Solution(object):
    def specialArray(self, nums):
        n = len(nums)
        nums.sort(reverse = True)
        
        i = 0
        while i < n and nums[i] > i:
            i+=1
        
        return -1 if i < len(nums) and i == nums[i] else i

        