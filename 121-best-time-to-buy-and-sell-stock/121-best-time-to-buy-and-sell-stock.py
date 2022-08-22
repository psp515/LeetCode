import heapq

class Solution(object):
    def maxProfit(self, prices):
        minheap = []
        maximal = 0
        for x in prices:
            heappush(minheap, x)
            mini = heappop(minheap)
            maximal = max(maximal, x - mini)
            heappush(minheap, mini)
            
        
        return maximal
        
        