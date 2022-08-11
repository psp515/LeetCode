# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def _nodeLen(self, node):
        n = 0
        while node:
            node = node.next
            n += 1
        return n
        
    def removeNthFromEnd(self, head, n):
        index_to_delete = self._nodeLen(head) - n
        
        i = 0
        iterable = head
        prev = ListNode(-1, head)
        main = prev
        
        while head != None:
            if i == index_to_delete:
                prev.next = iterable.next
                break
            prev = iterable
            iterable = iterable.next            
            i += 1
        
        return main.next
            
        