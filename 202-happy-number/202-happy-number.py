class Solution(object):
    def next(self, n):
        sum = 0
        
        while n:
            digit = n % 10
            n //= 10
            sum += digit*digit
        
        return sum
    
    def isHappy(self, n):
        d = {}
        while n != 1:
            if n in d:
                return False
            d[n] = True
            n = self.next(n)         
            
        return True