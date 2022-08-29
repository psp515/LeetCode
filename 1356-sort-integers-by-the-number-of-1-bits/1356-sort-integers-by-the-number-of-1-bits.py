class Solution(object):
    def get_bits(self, n):
        count = 0
        while n:
            count += n % 2
            n //= 2
        
        return count
    
    def sortByBits(self, arr):
        n = len(arr)
        arr = [(arr[i], self.get_bits(arr[i])) for i in range(n)]
        arr.sort(key=lambda x:x[0])
        arr.sort(key=lambda x:x[1])
        return [arr[i][0] for i in range(n)]
        