class Solution(object):
    def numberOfArithmeticSlices(self, arr):
        n=len(arr)
        l=[0]*(n)
        for i in range(2, n):
            if arr[i]-arr[i-1] == arr[i-1]-arr[i-2]:
                l[i]=1+l[i-1]
        return sum(l)
                
        