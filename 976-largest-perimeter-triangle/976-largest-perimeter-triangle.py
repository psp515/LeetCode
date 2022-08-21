class Solution(object):
    def largestPerimeter(self, arr):
        arr.sort(reverse = True)
        
        for i in range(2, len(arr)):
            if arr[i-2] >= arr[i-1] + arr[i]:
                continue
                
            return arr[i] + arr[i-1] + arr[i-2]
                
        return 0
        