# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
     def mergeKLists(self, lists):
        heap = []
        main = ListNode()
        head = main

        for x in lists:
            if x != None and x.val != None:
                tupl = (x.val, x)
                heapq.heappush(heap, tupl)

        while len(heap):
            value, item = heapq.heappop(heap)
            next = item.next
            item.next = None
            main.next = item
            main = main.next
            if next != None:
                heapq.heappush(heap, (next.val, next))

        return head.next
        