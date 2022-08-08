# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_node_len(self, node):
        len = 0
        while node != None:
            node = node.next
            len += 1
        return len
    
    def addNumbers(self, longer, shorter):
        head = longer
        carry_flag = False
        prev = None
        while longer != None:
            if shorter != None:
                value = longer.val + shorter.val 
                shorter = shorter.next
            else:
                value = longer.val
            
            if carry_flag:
                value += 1
                carry_flag = False
                
            if value > 9:
                carry_flag = True
            
            longer.val = value % 10
            prev = longer
            longer = longer.next
        
        if carry_flag:
            prev.next = ListNode(1)
        
        return head
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):         
        return self.addNumbers(l1,l2) if self.get_node_len(l1) > self.get_node_len(l2) else self.addNumbers(l2, l1)
        