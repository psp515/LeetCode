class Solution(object):
    def searchInsert(self, arr, target):
        s,e = 0, len(arr)-1
        
        while (s <= e):
            q = s + (e - s) // 2
            if (target == arr[q]):
                return q
            elif (target > arr[q]):
                s = q + 1
            else:
                e = q - 1
                
        return s
            
        