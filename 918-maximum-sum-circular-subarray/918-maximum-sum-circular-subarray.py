class Solution(object):
    def kadane(self, a):
        Max = a[0]
        temp = Max
        for i in range(1,len(a)):
            temp += a[i]
            if temp < a[i]:
                temp = a[i]
            Max = max(Max,temp)
        return Max

    def maxSubarraySumCircular(self, arr):
        n = len(arr)

        max_kadane = self.kadane(arr)
 
        neg_arr = [-1*x for x in arr]
        max_neg_kadane = self.kadane(neg_arr)
 
        max_wrap = -(sum(neg_arr)-max_neg_kadane)
 
        res = max(max_wrap, max_kadane)
    
        return res if res != 0  else max_kadane
        