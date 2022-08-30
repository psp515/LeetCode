class Solution(object):
    def shortestPathLength(self, G):
        n = len(G)
        result = 0
        visited_node = []
        stack = []  
        for i in range(n):
            visited_node.append(set([1<<i]))
            stack.append([i,1<<i])
            
        while stack:
            new_stack = []
            result += 1
            
            for i, value in stack:
                for u in G[i]:
                    x = (1<<u)|value
                    if x not in visited_node[u]:
                        if x+1 == 1<<n:
                            return result
                        
                        visited_node[u].add(x)
                        new_stack.append([u, x])
                        
            stack = new_stack
            
        return 0
        
        