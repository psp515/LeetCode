# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def get_max_pow(self, head):
        n = 0
        while head:
            n+=1
            head = head.next
        
        return n
    
    def getDecimalValue(self, head):
        n = self.get_max_pow(head) - 1
        number = 0
        
        while head:
            number += head.val * 2**n
            n-=1
            head = head.next
        
        return number
        