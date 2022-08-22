class Solution(object):
    def calc(self, i, j, v1, v2):
        return v2 + v1 + i - j
    
    def maxScoreSightseeingPair(self, arr):
        i = 0
        n = len(arr)
        maximal = - float("inf")
        
        for j in range(1, n):
            maximal = max(maximal, self.calc(i, j, arr[i], arr[j]))
            
            if i + arr[i] < j + arr[j]:
                i = j
        
        return maximal