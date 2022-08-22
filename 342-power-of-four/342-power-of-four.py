class Solution(object):
    def log4(self, x):
        return (math.log10(x) / math.log10(4));
    
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        
        return (math.ceil(self.log4(n)) == math.floor(self.log4(n)));
        