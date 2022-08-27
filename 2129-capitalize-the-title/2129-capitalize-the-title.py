class Solution(object):
    def capitalizeTitle(self, t):
        arr = t.split(' ')
        
        for i in range(len(arr)):
            if len(arr[i]) <= 2:
                arr[i] = lower(arr[i])
            else:
                arr[i] = arr[i].title()
        
        return " ".join(arr)
                
        