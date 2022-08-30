class Solution(object):
    def issafevisit(self, i, graph, visited, is_safe):

        if visited[i] == True:
            is_safe[i] = -1
            return -1

        visited[i] = True

        if any(x == i for x in graph[i]):
            is_safe[i] = -1
            return -1

        if len(graph[i]) == 0:
            return 1

        for x in graph[i]:

            if is_safe[x] == 1:
                continue

            if is_safe[x] == 0:
                is_safe[x] = self.issafevisit(x, graph, visited, is_safe)
                if is_safe[x] == -1:
                    is_safe[i] = -1
                    return -1
                continue
                
            return -1

        return 1

    def eventualSafeNodes(self, graph):
        n = len(graph)
        is_safe = [0 for _ in range(n)]
        visited = [False for _ in range(n)]

        for i in range(n):
            if visited[i] == False:
                if len(graph[i]) == 0:
                    is_safe[i] = 1
                elif any(x == i for x in graph[i]):
                    is_safe[i] = -1
                else:
                    is_safe[i] = self.issafevisit(i, graph, visited, is_safe)

        return [i for i in range(n) if is_safe[i]==1]
        return [i for i in range(n) if is_safe[i]]