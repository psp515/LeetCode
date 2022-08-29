class Solution(object):
    def bs(self, s, arr, target):
        e = len(arr) - 1
        ind = - float('inf')
        while s <= e:
            m = (s + e) // 2
            if arr[m] >= target:
                s = m + 1
                ind = m
            else:
                e = m - 1
                
        return ind

    def maxDistance(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        z = min(n, m)
        maxi = 0
        
        for i in range(z):
            maxi = max(maxi, self.bs(i, nums2, nums1[i]) - i)

        return maxi
        