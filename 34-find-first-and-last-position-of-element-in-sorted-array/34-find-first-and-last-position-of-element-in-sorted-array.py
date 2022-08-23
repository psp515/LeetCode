class Solution(object):
    
    def bs_right(self, arr, value):
        l, r = 0, len(arr) - 1
        index = -1
        while l <= r:
            q = (l + r) // 2

            if arr[q] == value:
                index = q
                r = q - 1
            elif arr[q] > value:
                r = q - 1
            else:
                l = q + 1

        return index
    
    def bs_left(self, arr, value):
        l, r = 0, len(arr) - 1
        index = -1
        while l <= r:
            q = (l + r) // 2

            if arr[q] == value:
                index = q
                l = q + 1
            elif arr[q] > value:
                r = q - 1
            else:
                l = q + 1

        return index
    
    def searchRange(self, arr, target):
        
        x = self.bs_left(arr, target)
        
        if x == -1:
            return [-1,-1]
        
        y = self.bs_right(arr, target)
        
        return [y, x]
        
        
        