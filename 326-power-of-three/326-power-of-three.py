import math

class Solution(object):
    def log3(self, x):
        return (math.log10(x) / math.log10(3));
    
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        
        return (math.ceil(self.log3(n)) == math.floor(self.log3(n)));
        