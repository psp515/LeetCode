class Solution(object):
    def bs(self, s, e, arr, target):
        
        while s <= e:
            m = (s+e)// 2
            
            if arr[m] == target:
                return m
            elif arr[m] >= target:
                e = m - 1
            else:
                s = m + 1
        
        return -1
    
    def bsm(self, arr, target):
        s, e = 0, len(arr) - 1
        index = -1 
        while s != e - 1 and s < e and e < len(arr):
            m = (s+e)// 2
            
            if arr[m] >= arr[s]:
                s = m 
            else:
                e = m
        
        return e
            
    def search(self, nums, target):
        mid = self.bsm(nums, target)
        
        x = self.bs(0, mid, nums, target)
        if x != -1:
            return x
        
        return self.bs(mid, len(nums)-1, nums, target)
        