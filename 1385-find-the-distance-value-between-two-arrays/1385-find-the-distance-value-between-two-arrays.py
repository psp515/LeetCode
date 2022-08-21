class Solution(object):
    
    def findTheDistanceValue(self, arr1, arr2, d):
        counter = 0
        for x in arr1:
            for z in arr2:
                if abs(x-z) <= d:
                    counter += 1
                    break
        
        return len(arr1) - counter
            
        