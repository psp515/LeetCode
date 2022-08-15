# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def len(self, head):
        i = 0
        while head:
            i += 1
            head = head.next
        return i
    
    def reverse(self, head):
        prev = None
        
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        
        return prev
        
    
    def pairSum(self, head):
        n = self.len(head)
        if n == 2:
            return head.val + head.next.val
        
        mid = n // 2
        
        i = 0
        prev = None
        middle = head
        
        while i < mid:
            i += 1
            prev = middle
            middle = middle.next
        
        prev.next = None
        middle = self.reverse(middle)
        
        maxs = 0
        while middle:
            maxs = max(maxs, middle.val + head.val)
            middle = middle.next
            head = head.next
        
        return maxs