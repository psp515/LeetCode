class Solution(object):
    def diff(self, a, b):
        c = 0
        for i in range(len(a)):
            if a[i]!= b[i]:
                c += 1
        return c
    
    def genify(self, a, b):
        ng = ""
        for i in range(len(a)):
            if a[i] == b[i]:
                ng += a[i]
            else:
                ng += b[i]
        return ng
    
    def minMutation(self, start, end, bank):
        
        stack = [(start, 0)]
        d = {}
        d[start] = True
        
        while stack:
            gene, c = stack.pop()
            if gene == end:
                return c
            
            for bankgene in bank:
                if self.diff(gene, bankgene) == 1:
                    ng = self.genify(gene, bankgene)
                    if ng in d:
                        continue
                    stack.append((ng,c+1))
                    d[ng] = True
        
        return -1
        