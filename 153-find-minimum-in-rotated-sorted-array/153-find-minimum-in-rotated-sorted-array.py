class Solution(object):
    def findMin(self, arr):
        
        
        s, e = 0, len(arr) - 1
        while s != e - 1 and s < e and e < len(arr):
            m = (s+e)// 2
            
            if arr[m] >= arr[s]:
                s = m 
            else:
                e = m
        
        return arr[e] if arr[e] < arr[0] else arr[0]
        