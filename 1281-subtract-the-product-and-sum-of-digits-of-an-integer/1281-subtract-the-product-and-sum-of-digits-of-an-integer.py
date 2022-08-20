class Solution(object):
    def subtractProductAndSum(self, n):
        m = 1
        s = 0
        
        while n:
            digit = n % 10
            m *= digit
            s += digit
            n //= 10
        
        return m - s
        