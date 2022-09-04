class Solution(object):
    def integerBreak(self, n):
        
        if n==2:
            return 1
        if n==3: 
            return 2
        
        output = 1;
        
        while n>4:
            output*=3;
            n-=3;
        
        output*=n;
        
        return output;
        