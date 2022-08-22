class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        diff = arr[0] - arr[1]
        for i in range(1, len(arr)):
            if diff != (arr[i-1] - arr[i]):
                return False
        
        return True
        