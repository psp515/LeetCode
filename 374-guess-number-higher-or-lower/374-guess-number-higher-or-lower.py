# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        s = 1
        e = n
        g = 1
        d = n // 2
        while g != 0:
            q = (e + s) // 2
            g = guess(q)
            if g == -1:
                e = q - 1
            else:
                s = q + 1
        
        return q 