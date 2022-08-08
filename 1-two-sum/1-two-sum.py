class Solution:
    def twoSum(self, nums: List[int], target: int):
        i, j = 0, len(nums) - 1
        nums = [[nums[i], i] for i in range(len(nums))]
        nums.sort(key=lambda x: x[0])
        while i < j:
            sum = nums[i][0] + nums[j][0]
            if sum == target:
                return [nums[i][1], nums[j][1]]
            elif sum < target:
                i += 1
            else:
                j -= 1
        return [0, 0]
        