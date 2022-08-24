class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        prefix = [0 for _ in range(n+1)]
        for i in range(n):
            prefix[i+1] = arr[i] + prefix[i]

        sum = 0
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    sum += arr[i]
                    continue
                if (j - i + 1) % 2 == 1:
                    sum += prefix[j+1] - prefix[i]
        return sum
        