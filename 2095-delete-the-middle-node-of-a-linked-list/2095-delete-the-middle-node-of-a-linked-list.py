# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def len(self, head):
        i=0
        while head:
            i+=1
            head = head.next
        return i
    
    def deleteMiddle(self, head):
        n = self.len(head)
        if n == 1:
            return None
        
        if n == 2:
            head.next = None
            return head
        
        main = head
        mid = n // 2
        prev = None
        i = 0
        
        while i < mid:
            i += 1
            prev = head
            head = head.next
        
        prev.next = head.next
        
        return main