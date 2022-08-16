class Solution(object):
    def countPoints(self, rings):
        ans = [[False,False,False] for i in range(10)]
        data = []
        
        data = []
        while rings:
            data.append((rings[0], int(rings[1])))
            rings = rings[2:]
        
        for item in data:
            if item[0]=="R":
                ans[item[1]][0] = True
            elif item[0]=="G":
                ans[item[1]][1] = True
            else:
                ans[item[1]][2] = True
        
        counter = 0
        for a,b,c in ans:
            if a and b and c:
                counter +=1
        
        return counter