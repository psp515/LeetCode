class Solution(object):
    def arraySign(self, nums):
        multi = 1
        for x in nums:
            if x < 0:
                multi *= -1
            elif x == 0:
                return 0
            
        return multi
        