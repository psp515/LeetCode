class Solution(object):
    def isPerfectSquare(self, num):
        return math.sqrt(num) == int(math.sqrt(num))
        