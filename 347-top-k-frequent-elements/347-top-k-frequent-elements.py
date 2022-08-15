class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}

        for element in nums:
            if element in d:
                d[element] += 1
            else:
                d[element] = 1

        data = list(d.items())
        data.sort(key=lambda x: x[1], reverse=True)

        data = [data[i][0] for i in range(len(data))]

        return data[:k]
        
        
    
    #def topKFrequent(self, nums, k):
    #    const = 10 ** 4
    #    buckets = [[0, i - const] for i in range(2 * const + 1)]
    #    for element in nums:
    #        index = element + const
    #        buckets[index][0] += 1
    #    buckets.sort(key=lambda x: x[0], reverse=True)
    #    values = []
    #    for i in range(k):
    #        values.append(buckets[i][1])
    #    return values