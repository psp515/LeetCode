# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head):
        prev = None
        
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        
        return prev
        
    
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        
        counter = 1
        group_head = head
        group_prev = ListNode(-1, head)
        main = group_prev
        
        while head:
            if counter == k:
                counter = 1
                next = head.next
                head.next = None
                
                reversed_head = self.reverse(group_head)
                group_prev.next = reversed_head
                group_head.next = next
                
                group_prev = group_head
                group_head = next
                head = next
            else:
                counter += 1
                head = head.next
                
        
        return main.next
            
        