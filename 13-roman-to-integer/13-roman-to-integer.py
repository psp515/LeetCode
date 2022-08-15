class Solution(object):
    def map(self, letter):
        if letter == "I":
            return 1
        if letter == "V":
            return 5
        if letter == "X":
            return 10
        if letter == "L":
            return 50
        if letter == "C":
            return 100
        if letter == "D":
            return 500
        
        return 1000
        
    
    def romanToInt(self, s):
        sum = 0
        prev = 0
        for i in range(len(s)-1, -1, -1):
            val = self.map(s[i])
            if val < prev:
                sum -= val
                prev = val
            else:
                sum += val
                prev = val
        
        return sum