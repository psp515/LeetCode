class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        
        if x == 1:
            return 1
        
        i = 1     
        while (i+1)*(i+1) <= x:
            i+=1
        
        return i
        