class Solution(object):
    def arrangeCoins(self, n):
        row = 0
        i = 1
        while n - i >= 0:
            row +=1
            n-=i
            i+=1
        return row
        