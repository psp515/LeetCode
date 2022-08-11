# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        prev = ListNode(-1, head)
        main = prev
            
        while head:
            if head.val != val:
                prev = head
                head = head.next
            else:
                prev.next = head.next
                head = head.next
        
        return main.next
        
        