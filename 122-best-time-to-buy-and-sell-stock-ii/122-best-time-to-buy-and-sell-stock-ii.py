class Solution(object):
    def isd(self, arr):
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                return False
        
        return True
    
    def maxProfit(self, arr):

        n = len(arr)
        sum = 0
        
        cost = arr[0]
        for i in range(1, n):
            if arr[i] < cost:
                cost = arr[i]
            elif arr[i] > cost:
                sum += arr[i] - cost
                cost = arr[i]
        
        return sum
            
        