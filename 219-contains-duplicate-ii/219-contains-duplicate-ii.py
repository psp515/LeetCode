class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort(key=lambda x:x[0])
        for i in range(1, len(nums)):
            if nums[i][0] == nums[i-1][0] and abs(nums[i][1] - nums[i-1][1]) <=k:
                return True
        return False 
        