class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        ret = []
        
        for item in items2:
            items1.append(item)
        
        items1.sort(key=lambda x:x[0])
        
        ret.append(items1[0])
        j = 0
        for i in range(1, len(items1)):
            act_val = ret[j][0]
            if act_val == items1[i][0]:
                ret[j][1] += items1[i][1]
            else:
                ret.append(items1[i])
                j += 1

        return ret
        