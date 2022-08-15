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
    
    def get_node(self, head, mid):
        i = 0 
        while i < mid:
            i += 1
            head = head.next
        
        return head
    
    def reverse(self, head):
        prev = None
        
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        
        return prev
    
    def are_the_same(self, arr1, arr2):
        while arr1 and arr2:
            if arr1.val != arr2.val:
                return False
            arr1 = arr1.next
            arr2 = arr2.next
        
        return True
    
    def isPalindrome(self, head):
        n = self.len(head)
        
        if n == 1:
            return True
        
        if n == 2:
            if head.val == head.next.val:
                return True
            return False
        
        mhead = ListNode()
        if n % 2 == 1:
            mid = n // 2
            mhead = self.get_node(head, mid).next  
        else:
            mid = n // 2
            mhead = self.get_node(head, mid)
        
        return self.are_the_same(head, self.reverse(mhead))
        