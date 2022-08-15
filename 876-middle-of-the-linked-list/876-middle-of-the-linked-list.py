# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def len(self, head):
        i = 0 
        while head:
            i+=1
            head = head.next
        
        return i
    
    def middleNode(self, head):
        index = self.len(head) / 2
        
        i = 0 
        while i < index:
            i += 1
            head = head.next
        
        return head
        