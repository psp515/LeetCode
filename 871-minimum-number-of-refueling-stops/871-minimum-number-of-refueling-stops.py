from heapq import *
class Solution(object):
    def minRefuelStops(self, target, fuel, stations):
        pq = []
        counter = 0
        act_pos = fuel

        stations.sort(key=lambda x: x[0])
        i = 0

        while act_pos < target:

            if i < len(stations) and stations[i][0] <= act_pos:
                heappush(pq, -stations[i][1])
                i += 1
                continue

            if act_pos < target and len(pq) == 0:
                return -1

            act_pos -= heappop(pq)
            counter += 1


        return counter
        