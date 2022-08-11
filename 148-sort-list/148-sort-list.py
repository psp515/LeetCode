# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution(object):
        
    def _heapsort(self, head):
        heap = []
        main = ListNode()
        _head = main
        
        while head:
            next = head.next
            head.next = None
            heappush(heap, (head.val, head))
            head = next
        
        while heap:
            _, item = heappop(heap)
            main.next = item
            main = main.next
        
        return _head.next
    
    def sortList(self, head):
        return self._heapsort(head)
        
        