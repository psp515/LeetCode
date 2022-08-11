class Solution(object):
    def _numbify(self, a, b, is_positive = True):
        count = 0
        temp = 0
        
        for i in range(31, -1, -1):
            if (temp + (b << i) <= a):
                temp += b << i;
                count |= 1 << i;
        
        if is_positive:
            return count if count < 2147483648 else 2147483647
        
        return -count if count > -2147483648 else -2147483648
    
    def _is_positive(self, a, b):
        if (a>0 and b > 0)or(a<0 and b<0):
            return True
        
        return False
    
    def divide(self, dividend, divisor):
        return self._numbify(abs(dividend), abs(divisor), self._is_positive(dividend,divisor))
        