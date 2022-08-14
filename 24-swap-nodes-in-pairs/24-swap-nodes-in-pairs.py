# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        data = []
        while head:
            next = head.next
            head.next = None
            data.append(head)
            head = next
        
        for i in range(len(data)):
            if i % 2 == 1:
                data[i], data[i-1] = data[i-1], data[i]
        
        head = ListNode()
        main = head
        
        for x in data:
            head.next = x
            head = head.next
        
        return main.next
        
        