class Solution(object):
    def findKthPositive(self, arr, k):
        s, e = 0, len(arr)
        
        while s < e:
            q = (s+e) // 2
            
            if arr[q] - q - 1 < k:
                s = q + 1
            else:
                e = q
            
        return e + k
        
        