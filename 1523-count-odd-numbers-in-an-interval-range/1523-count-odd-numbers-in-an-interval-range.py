class Solution(object):
    def countOdds(self, low, high):
        count = (high - low) // 2
        isLow = low % 2 == 1
        isHigh = high % 2 == 1
        if isLow or isHigh:
            return count + 1
        else:
            return count
        
        