class Solution(object):
    def peakIndexInMountainArray(self, arr):
        n = len(arr)
        if n == 3:
            return 1
        
        s = 1
        e = n - 2
        
        while s < e:
            q = (s+e)//2
            
            if arr[q-1] < arr[q] and arr[q] > arr[q+1]:
                return q
            elif arr[q-1] > arr[q]:
                e = q - 1
            else:
                s = q + 1
        
        return (s + e) // 2
        
        